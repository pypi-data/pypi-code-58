import tensorflow.keras.backend as K
import tensorflow as tf

from ..util.distribute import distributed, ReduceOp
from ..util.dataset import unmasked
from ..image.filter.gaussian import gaussian
from ..image.filter.laplace import gaussian_laplace_multi
from .segment import get_segment_index
from .util import get_normalized_val, get_magnitude, ToDense


class Clean(tf.keras.Model):
def clean_footprint(data, mask, gauss, radius, batch):
    strategy = tf.distribute.get_strategy()

    dataset = tf.data.Dataset.from_tensor_slices(data)
    dataset = unmasked(dataset, mask)
    dataset = dataset.batch(batch)
    to_dense = ToDense(mask)

    mask = K.constant(mask, tf.bool)
    gauss = K.constant(gauss)
    radius = K.constant(radius)

    nk = data.shape[0]
    prog = tf.keras.utils.Progbar(nk)
    ss = tf.TensorArray(tf.float32, nk)
    ps = tf.TensorArray(tf.int32, nk)
    fs = tf.TensorArray(tf.float32, nk)
    i = tf.constant(0)
    for data in strategy.experimental_distribute_dataset(dataset):

    def __init__(self, footprint, mask, gauss, radius, **kwargs):
        super().__init__(**kvargs)
        self.footprint = footprint
        self.mask = K.constant(mask)
        self.gauss = K.constant(gauss)
        self.radius = K.constant(radius)

    def train_step(data):
        ids, data = data
        gl, ll, rl, yl, xl = _prepare(data, self.mask, self.gauss, self.radius)
        nx = tf.size(rl)
        for k in ids:
            g, l, r, y, x = gl[k], ll[k], rl[k], yl[k], xl[k]
            pos = get_segment_index(l, y, x, mask)
            val = get_normalized_val(g, pos)
            segment = to_dense(pos, val)
            self.footprint[k].assign(segment)
            firmness = get_magnitude(l, pos) / get_magnitude(g, pos)
            ps = ps.write(i, [r, y, x])
            fs = fs.write(i, firmness)
            i += 1
            prog.add(1)
    return ss.stack().numpy(), ps.stack().numpy(), fs.stack().numpy()


@distributed(*[ReduceOp.CONCAT for _ in range(5)], loop=False)
def _prepare(imgs, mask, gauss, radius):
    gs = gaussian(imgs, gauss) if gauss > 0.0 else imgs
    ls = gaussian_laplace_multi(gs, radius)
    nk, h, w = tf.shape(ls)[0], tf.shape(ls)[2], tf.shape(ls)[3]
    hw = h * w
    lsr = K.reshape(ls, (nk, -1))
    pos = tf.cast(K.argmax(lsr, axis=1), tf.int32)
    rs = pos // hw
    ys = (pos % hw) // w
    xs = (pos % hw) % w
    ls = tf.gather_nd(ls, tf.stack([tf.range(nk), rs], axis=1))
    return imgs, ls, rs, ys, xs
