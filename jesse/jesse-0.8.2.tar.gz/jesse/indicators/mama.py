from collections import namedtuple

import numpy as np
import talib

from jesse.helpers import get_candle_source

MAMA = namedtuple('MAMA', ['mama', 'fama'])


def mama(candles: np.ndarray, fastlimit=0.5, slowlimit=0.05, source_type="close", sequential=False) -> MAMA:
    """
    MAMA - MESA Adaptive Moving Average

    :param candles: np.ndarray
    :param fastlimit: float - default: 0.5
    :param slowlimit: float - default: 0.05
    :param source_type: str - default: "close"
    :param sequential: bool - default=False

    :return: MAMA(mama, fama)
    """
    if not sequential and len(candles) > 240:
        candles = candles[-240:]

    source = get_candle_source(candles, source_type=source_type)
    mama, fama = talib.MAMA(source, fastlimit=fastlimit, slowlimit=slowlimit)

    if sequential:
        return MAMA(mama, fama)
    else:
        return MAMA(mama[-1], fama[-1])
