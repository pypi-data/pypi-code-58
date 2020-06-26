from __future__ import print_function, absolute_import

import importlib
import re
import string
import unicodedata
from .compat import str as compat_str
from functools import wraps

try:
    # getfullargspec is not available in python2
    # getargspec is deprecated
    # try to use getfullargspec if possible
    from inspect import isclass, getfullargspec as getargspec
except ImportError:
    from inspect import getargspec, isclass

import attr
import sqlalchemy.orm
import sqlparse
import hashlib

from faker import Faker
from faker.providers import BaseProvider
from six import text_type, string_types
from sqlalchemy.engine.default import DefaultDialect
from sqlalchemy.sql.functions import FunctionElement
from sqlalchemy.sql.sqltypes import Date, DateTime, NullType, String

from recipe.compat import basestring, integer_types, str

# only expose the printing sql function
__all__ = [
    "prettyprintable_sql",
    "generate_faker_seed",
    "clean_unicode",
    "FakerAnonymizer",
    "FakerFormatter",
    "recipe_arg",
]


def generate_faker_seed(value):
    """Generate a seed value for faker. """
    if not isinstance(value, compat_str):
        value = compat_str(value)

    h = hashlib.new("md5")
    h.update(value.encode("utf-8"))
    return int(h.hexdigest()[:16], 16)


def recipe_arg(*args):
    """Decorator for recipe builder arguments.

    Promotes builder pattern by returning self.
    """

    def decorator(func):
        @wraps(func)
        def wrapper(self, *_args, **_kwargs):
            from recipe import Recipe, RecipeExtension, BadRecipe

            if isinstance(self, Recipe):
                recipe = self
            elif isinstance(self, RecipeExtension):
                recipe = self.recipe
            else:
                raise BadRecipe(
                    "recipe_arg can only be applied to"
                    "methods of Recipe or RecipeExtension"
                )

            if recipe._query is not None:
                recipe.reset()

            func(self, *_args, **_kwargs)
            return recipe

        return wrapper

    return decorator


class TestProvider(BaseProvider):
    """A demo faker provider for testing string providers"""

    def foo(self):
        return "foo"


class StringLiteral(String):
    """ Teach SA how to literalize various things. """

    def literal_processor(self, dialect):
        super_processor = super(StringLiteral, self).literal_processor(dialect)

        def process(value):
            if isinstance(value, integer_types):
                return str(value)
            if not isinstance(value, basestring):
                value = str(value)
            result = super_processor(value)
            if isinstance(result, bytes):
                result = result.decode(dialect.encoding)
            return result

        return process


def prettyprintable_sql(statement, dialect=None, reindent=True):
    """
    Generate an SQL expression string with bound parameters rendered inline
    for the given SQLAlchemy statement. The function can also receive a
    `sqlalchemy.orm.Query` object instead of statement.

    WARNING: Should only be used for debugging. Inlining parameters is not
             safe when handling user created data.
    """
    if isinstance(statement, sqlalchemy.orm.Query):
        if dialect is None:
            dialect = statement.session.get_bind().dialect
        statement = statement.statement

    # Generate a class that can handle encoding
    if dialect:
        DialectKlass = dialect.__class__
    else:
        DialectKlass = DefaultDialect

    class LiteralDialect(DialectKlass):
        colspecs = {
            # prevent various encoding explosions
            String: StringLiteral,
            # teach SA about how to literalize a datetime
            DateTime: StringLiteral,
            Date: StringLiteral,
            # don't format py2 long integers to NULL
            NullType: StringLiteral,
        }

    compiled = statement.compile(
        dialect=LiteralDialect(), compile_kwargs={"literal_binds": True}
    )
    return sqlparse.format(str(compiled), reindent=reindent)


WHITESPACE_RE = re.compile(r"\s+", flags=re.DOTALL | re.MULTILINE)


def replace_whitespace_with_space(s):
    """ Replace multiple whitespaces with a single space. """
    return WHITESPACE_RE.sub(" ", s)


def clean_unicode(value):
    """Convert value into ASCII bytes by brute force."""
    if not isinstance(value, string_types):
        value = text_type(value)
    try:
        return value.encode("ascii")
    except UnicodeEncodeError:
        value = unicodedata.normalize("NFKD", value)
        return value.encode("ascii", "ignore")


class AttrDict(dict):
    def __init__(self, *args, **kwargs):
        super(AttrDict, self).__init__(*args, **kwargs)
        self.__dict__ = self


def disaggregate(expr):
    if isinstance(expr, FunctionElement):
        return expr.clause_expr
    else:
        return expr


class FakerFormatter(string.Formatter):
    """A formatter that can get values from Faker generators."""

    def format_field(self, obj, format_spec):
        """

        :param obj: A faker Faker
        :param format_spec: a generator
        :return: A string generated by
        """
        generator = format_spec
        kwargs = {}
        if "|" in format_spec:
            try:
                newgenerator, potential_kwargs = format_spec.split("|")
                for part in potential_kwargs.split(","):
                    k, v = part.split("=")
                    if v == "None":
                        v = None
                    elif v == "True":
                        v = True
                    elif v == "False":
                        v = False
                    elif v.isdigit():
                        v = int(v)
                    kwargs[k] = v
                generator = newgenerator
            except ValueError:
                # If more than one "|"  don't try to parse
                # If the kwargs aren't of form x=y then don't try to parse
                pass

        value = None
        if callable(getattr(obj, generator)):
            c = getattr(obj, generator)
            argspec = getargspec(c)
            if len(argspec.args) == 1:
                value = getattr(obj, generator)()
            elif kwargs:
                value = getattr(obj, generator)(**kwargs)
            else:
                value = c

        if value is not None and not isinstance(value, basestring):
            value = str(value)
        return value or "Unknown fake generator"


@attr.s
class FakerAnonymizer(object):
    """Returns a deterministically generated fake value that depends on the
    input value. """

    format_str = attr.ib()
    postprocessor = attr.ib()
    locale = attr.ib(default="en_US")
    postprocessor = attr.ib(default=None)
    providers = attr.ib(default=None)

    def __attrs_post_init__(self):
        self.fake = Faker(self.locale)
        self.formatter = FakerFormatter()
        for p in self._clean_providers(self.providers):
            self.fake.add_provider(p)

    def _clean_providers(self, providers):
        """Convert a list of anonymizer providers into classes suitable for
        adding with faker.add_provider"""
        if not providers:
            return []

        if not isinstance(providers, (list, tuple)):
            providers = [providers]

        cleaned_providers = []
        for provider in providers:
            if isinstance(provider, basestring):
                # dynamically import the provider
                parts = provider.split(".")
                if len(parts) > 1:
                    _module = ".".join(parts[:-1])
                    _provider_class = parts[-1]
                    try:
                        _mod = importlib.import_module(_module)
                        _provider = getattr(_mod, _provider_class, None)
                        if _provider is None:
                            # TODO: log an issue, provider not found in module
                            continue
                        elif not issubclass(_provider, BaseProvider):
                            # TODO: log an issue, provider not generator
                            continue
                        else:
                            cleaned_providers.append(_provider)

                    except ImportError:
                        # TODO: log an issue, can't import module
                        continue
            elif isclass(provider) and issubclass(provider, BaseProvider):
                cleaned_providers.append(provider)
            else:
                # TODO: log an issue, provider is not an importable string
                #  or a ProviderBase
                continue

        return cleaned_providers

    def __call__(self, value):
        self.fake.seed_instance(generate_faker_seed(value))
        value = self.formatter.format(self.format_str, fake=self.fake)
        if self.postprocessor is None:
            return value
        else:
            return self.postprocessor(value)
