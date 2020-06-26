"""
Scrapy Item

See documentation in docs/topics/item.rst
"""

from pprint import pformat
try:
    from collections.abc import MutableMapping  # noqa
except ImportError:
    from collections import MutableMapping  # noqa

from abc import ABCMeta
import six



class BaseItem(object):
    """Base class for all scraped items."""
    pass


class Field(dict):
    """Container of field metadata"""


class ItemMeta(ABCMeta):

    def __new__(mcs, class_name, bases, attrs):
        classcell = attrs.pop('__classcell__', None)
        new_bases = tuple(base._class for base in bases if hasattr(base, '_class'))
        _class = super(ItemMeta, mcs).__new__(mcs, 'x_' + class_name, new_bases, attrs)

        fields = getattr(_class, 'fields', {})
        new_attrs = {}
        for n in dir(_class):
            v = getattr(_class, n)
            if isinstance(v, Field):
                fields[n] = v
            elif n in attrs:
                new_attrs[n] = attrs[n]

        new_attrs['fields'] = fields
        new_attrs['_class'] = _class
        if classcell is not None:
            new_attrs['__classcell__'] = classcell
        return super(ItemMeta, mcs).__new__(mcs, class_name, bases, new_attrs)


class DictItem(MutableMapping, BaseItem):

    fields = {}

    def __init__(self, *args, **kwargs):
        self._values = {}
        if args or kwargs:  # avoid creating dict for most common case
            for k, v in six.iteritems(dict(*args, **kwargs)):
                self[k] = v

    def __getitem__(self, key):
        return self._values[key]

    def __setitem__(self, key, value):
        if key in self.fields:
            self._values[key] = value
        else:
            raise KeyError("%s does not support field: %s" %
                (self.__class__.__name__, key))

    def __delitem__(self, key):
        del self._values[key]

    def __getattr__(self, name):
        if name in self.fields:
            return self._values[name]
            # raise AttributeError("Use item[%r] to get field value" % name)
        raise AttributeError(name)

    def __setattr__(self, key, value):
        if key.startswith('_'):
            super(DictItem, self).__setattr__(key, value)
        elif key in self.fields:
            self._values[key] = value
        else:
            raise KeyError("%s does not support field: %s" %
                (self.__class__.__name__, key))


    def __len__(self):
        return len(self._values)

    def __iter__(self):
        return iter(self._values)

    __hash__ = BaseItem.__hash__

    def keys(self):
        return self._values.keys()

    def __repr__(self):
        return pformat(dict(self))

    def copy(self):
        return self.__class__(self)

@six.add_metaclass(ItemMeta)
class Item(DictItem):
    pass

class Buyer(Item):
    name = Field()

class Map(Item):
    chal = Field()
    dal = Field()
    buyer = Field()

m = Map()
b = Buyer()
b.name = "John"

m.chal = 34
m.buyer = Buyer(name="John")
m.buyer.name = 'JLKJL'

print(dict(m))
