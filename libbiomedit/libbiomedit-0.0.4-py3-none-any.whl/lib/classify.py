import sys
from typing import Union, Tuple, Any, Dict, Optional, Sequence
import collections

import dataclasses

# Starting with python 3.7, the typing module has a new API
__origin_attr__ = "__extra__" if sys.version_info < (3, 7) else "__origin__"

_classifiers = []


def _classifier(T):
    """Decorator populating :_classifiers:"""
    def decorator(f):
        _classifiers.append((T, f))
        return f
    return decorator


def classify(T: type):
    try:
        return next(C for C, check in _classifiers if check(T))
    except StopIteration:
        return None


@_classifier(Any)
def classify_any(T: type) -> bool:
    return T is Any


@_classifier(Tuple)
def classify_tuple(T: type) -> bool:
    return getattr(T, __origin_attr__, None) is tuple


@_classifier(Sequence)
def classify_seq(T: type) -> bool:
    seq_type = getattr(T, __origin_attr__, None)
    return (isinstance(seq_type, type) and
            issubclass(seq_type, collections.abc.Sequence))


@_classifier(dataclasses.dataclass)
def classify_dataclass(T: type) -> bool:
    return dataclasses.is_dataclass(T)


@_classifier(Optional)
def classify_optional(T: type) -> bool:
    return (getattr(T, "__origin__", None) is Union and
            isinstance(None, T.__args__) and len(T.__args__) == 2)


@_classifier(Union)
def classify_union(T: type) -> bool:
    return getattr(T, "__origin__", None) is Union


@_classifier(Dict)
def classify_dict(T: type) -> bool:
    t_origin = getattr(T, __origin_attr__, None)
    return t_origin is dict
