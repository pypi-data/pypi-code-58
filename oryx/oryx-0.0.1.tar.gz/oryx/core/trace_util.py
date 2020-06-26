# Copyright 2020 The TensorFlow Probability Authors.
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
# ============================================================================
# Lint as: python3
"""Module for JAX tracing utility functions."""
import contextlib
from typing import Any, Dict, Generator, List

from jax import abstract_arrays
from jax import api_util
from jax import core as jax_core
from jax import linear_util as lu
from jax import tree_util
from jax import util as jax_util
from jax.interpreters import partial_eval as pe

safe_map = jax_util.safe_map


def get_shaped_aval(x):
  if hasattr(x, 'dtype') and hasattr(x, 'shape'):
    return abstract_arrays.ShapedArray(x.shape, x.dtype)
  return abstract_arrays.raise_to_shaped(jax_core.get_aval(x))


def pv_like(x, abstract=True):
  if abstract:
    return pe.PartialVal((get_shaped_aval(x), jax_core.unit))
  else:
    return pe.PartialVal((None, x))  # pytype: disable=wrong-arg-types


def stage(f):
  """Returns a function that stages a function to a TypedJaxpr and its Pytrees."""

  def wrapped(*args, **kwargs):
    fun = lu.wrap_init(f, kwargs)
    flat_args, in_tree = tree_util.tree_flatten(args)
    flat_fun, out_tree = api_util.flatten_fun_nokwargs(fun, in_tree)
    flat_avals = safe_map(get_shaped_aval, flat_args)
    pvals = [pe.PartialVal((aval, jax_core.unit)) for aval in flat_avals]
    jaxpr, out_pvals, consts = pe.trace_to_jaxpr(
        flat_fun,
        pvals,
        instantiate=True,
        stage_out=True,
        trace_type=pe.StagingJaxprTrace)
    out_avals = [pval.get_aval() for pval in out_pvals]
    typed_jaxpr = jax_core.TypedJaxpr(jaxpr, consts, flat_avals, out_avals)
    return typed_jaxpr, (in_tree, out_tree())

  return wrapped


def trees(f):

  def wrapped(*args, **kwargs):
    return stage(f)(*args, **kwargs)[1]

  return wrapped


dynamic_contexts: Dict[jax_core.MasterTrace, List[Any]] = {}


@contextlib.contextmanager
def new_dynamic_context(master: jax_core.MasterTrace,
                        context: Any) -> Generator[None, None, None]:
  """Creates a dynamic context for a trace."""
  if master not in dynamic_contexts:
    dynamic_contexts[master] = []
  dynamic_contexts[master].append(context)
  try:
    yield
  finally:
    dynamic_contexts[master].pop()
    if not dynamic_contexts[master]:
      del dynamic_contexts[master]


def get_dynamic_context(trace: jax_core.Trace) -> Any:
  """Returns the current active dynamic context for a trace."""
  if trace.master not in dynamic_contexts:
    raise ValueError(f'No dynamic context registered for trace: {trace}')
  return dynamic_contexts[trace.master][-1]
