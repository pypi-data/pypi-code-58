import tensorflow as tf
from tensorflow.python.ops import array_ops

EPSILON = 1e-8

def sigmoid_focal_loss (labels, logits, alpha = 0.25, gamma = 2):
    p = tf.nn.sigmoid (logits)
    zeros = array_ops.zeros_like (p, dtype = p.dtype)
    # For poitive prediction, only need consider front part loss, back part is 0;
    # target_tensor > zeros <=> z=1, so poitive coefficient = z - p.
    pos_p_sub = array_ops.where (labels > zeros, labels - p, zeros)
    # For negative prediction, only need consider back part loss, front part is 0;
    # target_tensor > zeros <=> z=1, so negative coefficient = 0.
    neg_p_sub = array_ops.where (labels > zeros, zeros, p)
    per_entry_cross_ent = - alpha * (pos_p_sub ** gamma) * tf.log (tf.clip_by_value (p, EPSILON, 1.0)) \
                          - (1 - alpha) * (neg_p_sub ** gamma) * tf.log (tf.clip_by_value(1.0 - p, EPSILON, 1.0))
    return tf.reduce_mean (tf.reduce_sum (per_entry_cross_ent, axis = 1))

def categorical_focal_loss (labels, logits, alpha = 0.25, gamma = 2):
  # Scale predictions so that the class probas of each sample sum to 1
  logits = tf.nn.softmax (logits)
  logits /= tf.reduce_sum (logits, axis=-1, keepdims=True)
  # Clip the prediction value to prevent NaN's and Inf's
  logits = tf.clip_by_value (logits, EPSILON, 1. - EPSILON)
  # Calculate Cross Entropy
  cross_entropy = -labels * tf.log (logits)
  # Calculate Focal Loss
  loss = alpha * tf.pow (1 - logits, gamma) * cross_entropy

  # Sum the losses in mini_batch
  return tf.reduce_mean (tf.reduce_sum (loss, axis = 1))

def binary_focal_loss (labels, logits, alpha = 0.25, gamma = 2):
  logits = tf.nn.sigmoid (logits)
  pt_1 = tf.where(tf.equal(labels, 1), logits, tf.ones_like(logits))
  pt_0 = tf.where(tf.equal(labels, 0), logits, tf.zeros_like(logits))

  # clip to prevent NaN's and Inf's
  pt_1 = tf.clip_by_value (pt_1, EPSILON, 1. - EPSILON)
  pt_0 = tf.clip_by_value (pt_0, EPSILON, 1. - EPSILON)

  return tf.reduce_mean (
          -tf.reduce_sum (alpha * tf.pow (1. - pt_1, gamma) * tf.log (pt_1))
          -tf.reduce_sum ((1 - alpha) * tf.pow (pt_0, gamma) * tf.log (1. - pt_0))
  )
