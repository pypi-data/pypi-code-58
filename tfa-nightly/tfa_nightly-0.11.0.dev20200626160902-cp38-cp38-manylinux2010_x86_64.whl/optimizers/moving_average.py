# Copyright 2019 The TensorFlow Authors. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ==============================================================================

import tensorflow as tf
from tensorflow.python.training.moving_averages import assign_moving_average
from tensorflow_addons.optimizers import AveragedOptimizerWrapper
from tensorflow_addons.utils import types

from typing import Optional
from typeguard import typechecked


@tf.keras.utils.register_keras_serializable(package="Addons")
class MovingAverage(AveragedOptimizerWrapper):
    """Optimizer that computes a moving average of the variables.

    Empirically it has been found that using the moving average of the trained
    parameters of a deep network is better than using its trained parameters
    directly. This optimizer allows you to compute this moving average and swap
    the variables at save time so that any code outside of the training loop
    will use by default the average values instead of the original ones.

    Example of usage:

    ```python
    opt = tf.keras.optimizers.SGD(learning_rate)
    opt = tfa.optimizers.MovingAverage(opt)

    ```
    """

    @typechecked
    def __init__(
        self,
        optimizer: types.Optimizer,
        sequential_update: bool = True,
        average_decay: types.FloatTensorLike = 0.99,
        num_updates: Optional[str] = None,
        start_step: int = 0,
        dynamic_decay: bool = False,
        name: str = "MovingAverage",
        **kwargs
    ):
        r"""Construct a new MovingAverage optimizer.

        Args:
            optimizer: str or `tf.keras.optimizers.Optimizer` that will be
                used to compute and apply gradients.
            sequential_update: Bool. If False, will compute the moving average
                at the same time as the model is updated, potentially doing
                benign data races. If True, will update the moving average
                after gradient updates.
            average_decay: float. Decay to use to maintain the moving averages
                of trained variables.
            num_updates: Optional count of the number of updates applied to
                variables.
            start_step: int. What step to start the moving average.
            dynamic_decay: bool. Whether to change the decay based on the number
                of optimizer updates. Decay will start at 0.1 and gradually
                increase up to `average_decay` after each optimizer update.
            name: Optional name for the operations created when applying
                gradients. Defaults to "MovingAverage".
            **kwargs: keyword arguments. Allowed to be {`clipnorm`,
                `clipvalue`, `lr`, `decay`}. `clipnorm` is clip gradients by
                norm; `clipvalue` is clip gradients by value, `decay` is
                included for backward compatibility to allow time inverse
                decay of learning rate. `lr` is included for backward
                compatibility, recommended to use `learning_rate` instead.
        """
        super().__init__(optimizer, sequential_update, name, **kwargs)
        self._num_updates = num_updates
        if self._num_updates is not None:
            num_updates = tf.cast(self._num_updates, tf.float32, name="num_updates")
            average_decay = tf.minimum(
                average_decay, (1.0 + num_updates) / (10.0 + num_updates)
            )

        self._set_hyper("average_decay", average_decay)
        self._start_step = start_step
        self._dynamic_decay = dynamic_decay

    @tf.function
    def _get_decay(self, step: tf.Tensor):
        average_decay = self._get_hyper("average_decay", tf.dtypes.float32)

        step = tf.cast(step, tf.float32)
        if step < self._start_step:
            return tf.constant(0.0, tf.float32)
        elif self._dynamic_decay:
            step_count = step - self._start_step
            return tf.minimum(average_decay, (1.0 + step_count) / (10.0 + step_count))
        else:
            return average_decay

    def average_op(self, var, average_var):
        decay = self._get_decay(self._optimizer.iterations)
        return assign_moving_average(average_var, var, decay, False)

    def get_config(self):
        config = {
            "average_decay": self._serialize_hyperparameter("average_decay"),
            "num_updates": self._num_updates,
            "start_step": self._start_step,
            "dynamic_decay": self._dynamic_decay,
        }
        base_config = super().get_config()
        return {**base_config, **config}

    def _create_slots(self, var_list):
        self._optimizer._create_slots(
            var_list=var_list
        )  # pylint: disable=protected-access
        for var in var_list:
            self.add_slot(var, "average", var.read_value())

    def shadow_copy(self, model_weights):
        """Creates shadow variables for the given model weights."""
        for var in model_weights:
            self.add_slot(var, "average", initializer="zeros")
        self._average_weights = [self.get_slot(var, "average") for var in model_weights]
        self._model_weights = model_weights

    @property
    def has_shadow_copy(self):
        """Whether this optimizer has created shadow variables."""
        return self._model_weights is not None

    def swap_weights(self):
        """Swap the average and moving weights.

      This is a convenience method to allow one to evaluate the averaged weights
      at test time. Loads the weights stored in `self._average_weights` into the model,
      keeping a copy of the original model weights. Swapping twice will return
      the original weights.
      """
        if tf.distribute.in_cross_replica_context():
            strategy = tf.distribute.get_strategy()
            return strategy.run(self._swap_weights, args=())
        else:
            raise ValueError(
                "Swapping weights must occur under a " "tf.distribute.Strategy"
            )

    @tf.function
    def _swap_weights(self):
        def fn_0(a, b):
            a.assign_add(b)
            return a

        def fn_1(b, a):
            b.assign(a - b)
            return b

        def fn_2(a, b):
            a.assign_sub(b)
            return a

        def swap(strategy, a, b):
            """Swap `a` and `b` and mirror to all devices."""
            for a_element, b_element in zip(a, b):
                strategy.extended.update(
                    a_element, fn_0, args=(b_element,)
                )  # a = a + b
                strategy.extended.update(
                    b_element, fn_1, args=(a_element,)
                )  # b = a - b
                strategy.extended.update(
                    a_element, fn_2, args=(b_element,)
                )  # a = a - b

        ctx = tf.distribute.get_replica_context()
        return ctx.merge_call(swap, args=(self._average_weights, self._model_weights,))
