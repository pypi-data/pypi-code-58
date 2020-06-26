"""Modified JSON API v1.0 for OPTIMADE API"""
# pylint: disable=no-self-argument,no-name-in-module
from enum import Enum

from pydantic import Field, root_validator, BaseModel, AnyHttpUrl, AnyUrl, EmailStr
from typing import Optional, Union, List

from datetime import datetime

from . import jsonapi
from .utils import SemanticVersion


__all__ = (
    "DataType",
    "ResponseMetaQuery",
    "Provider",
    "ImplementationMaintainer",
    "Implementation",
    "ResponseMeta",
    "OptimadeError",
    "Success",
    "Warnings",
    "BaseRelationshipMeta",
    "BaseRelationshipResource",
    "Relationship",
)


class DataType(Enum):
    """Optimade Data Types

See the section "Data types" in the OPTIMADE API specification for more information.
    """

    STRING = "string"
    INTEGER = "integer"
    FLOAT = "float"
    BOOLEAN = "boolean"
    TIMESTAMP = "timestamp"
    LIST = "list"
    DICTIONARY = "dictionary"
    UNKNOWN = "unknown"

    @classmethod
    def get_values(cls):
        """Get OPTIMADE data types (enum values) as a (sorted) list"""
        return sorted((_.value for _ in cls))

    @classmethod
    def from_python_type(cls, python_type: Union[type, str, object]):
        """Get OPTIMADE data type from a Python type"""
        mapping = {
            "bool": cls.BOOLEAN,
            "int": cls.INTEGER,
            "float": cls.FLOAT,
            "complex": None,
            "generator": cls.LIST,
            "list": cls.LIST,
            "tuple": cls.LIST,
            "range": cls.LIST,
            "hash": cls.INTEGER,
            "str": cls.STRING,
            "bytes": cls.STRING,
            "bytearray": None,
            "memoryview": None,
            "set": cls.LIST,
            "frozenset": cls.LIST,
            "dict": cls.DICTIONARY,
            "dict_keys": cls.LIST,
            "dict_values": cls.LIST,
            "dict_items": cls.LIST,
            "NoneType": cls.UNKNOWN,
            "None": cls.UNKNOWN,
            "datetime": cls.TIMESTAMP,
            "date": cls.TIMESTAMP,
            "time": cls.TIMESTAMP,
            "datetime.datetime": cls.TIMESTAMP,
            "datetime.date": cls.TIMESTAMP,
            "datetime.time": cls.TIMESTAMP,
        }

        if isinstance(python_type, type):
            python_type = python_type.__name__
        elif isinstance(python_type, object):
            if str(python_type) in mapping:
                python_type = str(python_type)
            else:
                python_type = type(python_type).__name__

        return mapping.get(python_type, None)

    @classmethod
    def from_json_type(cls, json_type: str):
        """Get OPTIMADE data type from a named JSON type"""
        mapping = {
            "string": cls.STRING,
            "integer": cls.INTEGER,
            "number": cls.FLOAT,  # actually includes both integer and float
            "object": cls.DICTIONARY,
            "array": cls.LIST,
            "boolean": cls.BOOLEAN,
            "null": cls.UNKNOWN,
            # OpenAPI "format"s:
            "double": cls.FLOAT,
            "float": cls.FLOAT,
            "int32": cls.INTEGER,
            "int64": cls.INTEGER,
            "date": cls.TIMESTAMP,
            "date-time": cls.TIMESTAMP,
            "password": cls.STRING,
            "byte": cls.STRING,
            "binary": cls.STRING,
            # Non-OpenAPI "format"s, but may still be used by pydantic/FastAPI
            "email": cls.STRING,
            "uuid": cls.STRING,
            "uri": cls.STRING,
            "hostname": cls.STRING,
            "ipv4": cls.STRING,
            "ipv6": cls.STRING,
        }

        return mapping.get(json_type, None)


class OptimadeError(jsonapi.Error):
    """detail MUST be present"""

    detail: str = Field(
        ...,
        description="A human-readable explanation specific to this occurrence of the problem.",
    )


class Warnings(OptimadeError):
    """OPTIMADE-specific warning class based on OPTIMADE-specific JSON API Error.

From the specification:

A warning resource object is defined similarly to a JSON API error object, but MUST also include the field type, which MUST have the value "warning".
The field detail MUST be present and SHOULD contain a non-critical message, e.g., reporting unrecognized search attributes or deprecated features.

Note: Must be named "Warnings", since "Warning" is a built-in Python class.
"""

    type: str = Field(
        "warning", const=True, description='Warnings must be of type "warning"'
    )

    @root_validator(pre=True)
    def status_must_not_be_specified(cls, values):
        if values.get("status", None) is not None:
            raise ValueError("status MUST NOT be specified for warnings")
        return values


class ResponseMetaQuery(BaseModel):
    """ Information on the query that was requested. """

    representation: str = Field(
        ...,
        description="a string with the part of the URL that follows the base URL. Example: '/structures?'",
    )


class Provider(BaseModel):
    """Information on the database provider of the implementation."""

    name: str = Field(..., description="a short name for the database provider")

    description: str = Field(
        ..., description="a longer description of the database provider"
    )

    prefix: str = Field(
        ..., description="database-provider-specific prefix as found in " "Appendix 1."
    )

    homepage: Optional[Union[AnyHttpUrl, jsonapi.Link]] = Field(
        None,
        description="a [JSON API links object](http://jsonapi.org/format/1.0#document-links) "
        "pointing to homepage of the database provider, either "
        "directly as a string, or as a link object.",
    )

    index_base_url: Optional[Union[AnyHttpUrl, jsonapi.Link]] = Field(
        None,
        description="a [JSON API links object](http://jsonapi.org/format/1.0#document-links) "
        "pointing to the base URL for the `index` meta-database as "
        "specified in Appendix 1, either directly as a string, or "
        "as a link object.",
    )


class ImplementationMaintainer(BaseModel):
    """Details about the maintainer of the implementation"""

    email: EmailStr = Field(..., description="the maintainer's email address")


class Implementation(BaseModel):
    """Information on the server implementation"""

    name: Optional[str] = Field(None, description="name of the implementation")

    version: Optional[str] = Field(
        None, description="version string of the current implementation"
    )

    source_url: Optional[AnyUrl] = Field(
        None,
        description="URL of the implementation source, either downloadable archive or version control system",
    )

    maintainer: Optional[ImplementationMaintainer] = Field(
        None,
        description="A dictionary providing details about the maintainer of the implementation.",
    )


class ResponseMeta(jsonapi.Meta):
    """
    A [JSON API meta member](https://jsonapi.org/format/1.0#document-meta)
    that contains JSON API meta objects of non-standard
    meta-information.

    OPTIONAL additional information global to the query that is not
    specified in this document, MUST start with a
    database-provider-specific prefix.
    """

    query: ResponseMetaQuery = Field(
        ..., description="Information on the Query that was requested"
    )

    api_version: SemanticVersion = Field(
        ..., description="A string containing the version of the API implementation.",
    )

    time_stamp: datetime = Field(
        ...,
        description="A timestamp containing the date and time at which the query was executed.",
    )

    data_returned: int = Field(
        ...,
        description="An integer containing the total number of data resource objects returned for the current `filter` query, independent of pagination.",
        ge=0,
    )

    more_data_available: bool = Field(
        ...,
        description="`false` if all data resource objects for this `filter` query have been returned in the response or if it is the last page of a paginated response, and `true` otherwise.",
    )

    provider: Provider = Field(
        ..., description="information on the database provider of the implementation."
    )

    data_available: Optional[int] = Field(
        None,
        description="An integer containing the total number of data resource objects available in the database for the endpoint.",
    )

    last_id: Optional[str] = Field(
        None, description="a string containing the last ID returned"
    )

    response_message: Optional[str] = Field(
        None, description="response string from the server"
    )

    implementation: Optional[Implementation] = Field(
        None, description="a dictionary describing the server implementation"
    )

    warnings: Optional[List[Warnings]] = Field(
        None,
        description="""A list of warning resource objects representing non-critical errors or warnings.
A warning resource object is defined similarly to a [JSON API error object](http://jsonapi.org/format/1.0/#error-objects), but MUST also include the field `type`, which MUST have the value `"warning"`.
The field `detail` MUST be present and SHOULD contain a non-critical message, e.g., reporting unrecognized search attributes or deprecated features.
The field `status`, representing a HTTP response status code, MUST NOT be present for a warning resource object.
This is an exclusive field for error resource objects.""",
        uniqueItems=True,
    )


class Success(jsonapi.Response):
    """errors are not allowed"""

    meta: Optional[ResponseMeta] = Field(
        None, description="A meta object containing non-standard information"
    )

    @root_validator(pre=True)
    def either_data_meta_or_errors_must_be_set(cls, values):
        """Overwriting the existing validation function, since 'errors' MUST NOT be set"""
        required_fields = ("data", "meta")
        if not any(values.get(field) for field in required_fields):
            raise ValueError(
                f"At least one of {required_fields} MUST be specified in the top-level response"
            )

        # errors MUST be skipped
        if values.get("errors", None) is not None:
            raise ValueError("'errors' MUST be skipped for a successful response")

        return values


class BaseRelationshipMeta(jsonapi.Meta):
    """Specific meta field for base relationship resource"""

    description: str = Field(
        ..., description="OPTIONAL human-readable description of the relationship"
    )


class BaseRelationshipResource(jsonapi.BaseResource):
    """Minimum requirements to represent a relationship resource"""

    meta: Optional[BaseRelationshipMeta] = Field(
        None,
        description="Relationship meta field. MUST contain 'description' if supplied.",
    )


class Relationship(jsonapi.Relationship):
    """Similar to normal JSON API relationship, but with addition of OPTIONAL meta field for a resource"""

    data: Optional[
        Union[BaseRelationshipResource, List[BaseRelationshipResource]]
    ] = Field(None, description="Resource linkage", uniqueItems=True)
