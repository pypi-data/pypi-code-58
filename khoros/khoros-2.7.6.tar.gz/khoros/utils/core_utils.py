# -*- coding: utf-8 -*-
"""
:Module:            khoros.utils.core_utils
:Synopsis:          Collection of supporting utilities and functions to complement the primary modules
:Usage:             ``from khoros.utils import core_utils``
:Example:           ``encoded_string = core_utils.encode_url(decoded_string)``
:Created By:        Jeff Shurtliff
:Last Modified:     Jeff Shurtliff
:Modified Date:     25 May 2020
"""

import os
import random
import string
import warnings
import subprocess
import urllib.parse
from html import unescape

from .. import errors


def url_encode(raw_string):
    """This function encodes a string for use in URLs.

    :param raw_string: The raw string to be encoded
    :type raw_string: str
    :returns: The encoded string
    """
    return urllib.parse.quote_plus(raw_string)


def url_decode(encoded_string):
    """This function decodes a url-encoded string.

    :param encoded_string: The url-encoded string
    :type encoded_string: str
    :returns: The unencoded string
    """
    return urllib.parse.unquote_plus(encoded_string)


def decode_html_entities(html_string):
    """This function converts HTML entities (e.g. ``&amp;``, ``&apos;``, etc.) back to their original characters.

    :param html_string: The string containing HTML entities to be decoded
    :type html_string: str
    :returns: The string with decoded HTML entities
    """
    return unescape(html_string)


def decode_binary(binary):
    """This function decodes a binary into a UTF-8 encoded string.

    .. versionadded:: 2.6.0

    :param binary: The binary to be decoded
    :returns: The properly decoded string
    :raises: :py:exc:`TypeError`, :py:exc:`ValueError`
    """
    return binary.decode('utf-8')


def run_cmd(cmd, return_type='dict', shell=True, decode_output=True, strip_output=False,
            exclude_stdout=False, exclude_stderr=False, exclude_return_code=False):
    """This function executes a shell command on the operating system.

    .. versionadded:: 2.5.1

    :param cmd: The command to be executed
    :type cmd: str
    :param return_type: Determines the format in which the results should be returned (``dict`` by default)
    :type return_type: str
    :param shell: Determines if the ``shell`` argument in the :py:func:`subprocess.run` function should be ``True``
    :type shell: bool
    :param decode_output: Determines if the binary output should be decoded as a UTF-8 string (``True`` by default)
    :type decode_output: bool
    :param strip_output: Determines if the escape character(s) should be stripped from the output (``False`` by default)
    :type strip_output: bool
    :param exclude_stdout: Determines if the ``stdout`` output should be excluded (``False`` by default)
    :type exclude_stdout: bool
    :param exclude_stderr: Determines if the ``stderr`` output should be excluded (``False`` by default)
    :type exclude_stderr: bool
    :param exclude_return_code: Determines if the return code from the command should be excluded (``False`` by default)
    :type exclude_return_code: bool
    :returns: The results from the executed script
    :raises: :py:exc:`khoros.errors.exceptions.MissingRequiredDataError`
    """
    if exclude_stdout and exclude_stderr and exclude_return_code:
        raise errors.exceptions.MissingRequiredDataError("At least one output type must be enabled.")
    output = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=shell)
    stdout, stderr, return_code = output.stdout, output.stderr, output.returncode
    results = {
        'stdout': stdout,
        'stderr': stderr,
        'return_code': return_code
    }
    for stream in ('stdout', 'stderr'):
        if decode_output:
            results[stream] = decode_binary(results.get(stream))
        if strip_output:
            results[stream] = results.get(stream).strip()
    output_types = {'stdout': exclude_stdout, 'stderr': exclude_stderr, 'return_code': exclude_return_code}
    for output_type, excluded in output_types.items():
        if excluded:
            del results[output_type]
    if return_type == 'list':
        results = list(results.values())
    elif return_type == 'tuple':
        results = tuple(results.values())
    else:
        if return_type != 'dict':
            raise ValueError(f"'{return_type}' is not a valid return type.")
    return results


def _is_zero_length(_element):
    """This function checks to see if an element has a zero length.

    :param _element: The element of which the length will be checked
    :returns: Boolean value stating whether or not the length of the element is zero
    """
    return True if len(_element) == 0 else False


def _structure_query_string(_url_dict, _no_encode):
    """This function constructs a query string where one or more fields must not be URL-encoded.

    :param _url_dict: Dictionary of URL query string keys and values
    :type _url_dict: dict
    :param _no_encode: Designates any dictionary keys (i.e. field names) whose values should not be URL-encoded
    :type _no_encode: list, tuple, set, str, None
    :returns: The URL query string in string format
    """
    if type(_no_encode) == str:
        _no_encode = (_no_encode, )
    _delimiters = {True: "", False: "&"}
    _query_string = ""
    for _field_name, _field_value in _url_dict.items():
        if _field_name not in _no_encode:
            _field_value = url_encode(_field_value)
        _delimiter = _delimiters.get(_is_zero_length(_query_string))
        _query_string = f"{_query_string}{_delimiter}{_field_name}={_field_value}"
    return _query_string


def encode_query_string(url_dict, no_encode=None):
    """This function compiles a URL query string from a dictionary of parameters.

    :param url_dict: Dictionary of URL query string keys and values
    :type url_dict: dict
    :param no_encode: Designates any dictionary keys (i.e. field names) whose values should not be URL-encoded
    :type no_encode: list, tuple, set, str, None
    :returns: The URL query string in string format
    """
    if no_encode:
        query_string = _structure_query_string(url_dict, no_encode)
    else:
        query_string = urllib.parse.urlencode(url_dict)
    return query_string


def is_numeric(value):
    """This function checks whether or not a value is numeric either as an integer or a numeric string.

    .. versionadded:: 2.3.0

    :param value: The value to be examined
    :type value: str, int
    :returns: Boolean value indicating if the examined value is numeric
    """
    return True if type(value) == int or (type(value) == str and value.isnumeric()) else False


def convert_set(iterable, convert_to='list'):
    """This function casts a ``set`` variable to be a ``list`` instead so that it can be scriptable.

    :param iterable: The iterable to be evaluated to see if it has a ``set`` type
    :param convert_to: Defines if the iterable should be cast to a ``list`` (default) or a ``tuple``
    :type convert_to: str
    :returns: The converted variable as a ``list`` or ``tuple`` (or untouched if not a ``set``)
    """
    if type(iterable) == set:
        if convert_to == 'tuple':
            iterable = tuple(iterable)
        else:
            iterable = list(iterable)
    return iterable


def convert_single_value_to_tuple(value):
    """This function converts a single value of nearly any type into a tuple.

    .. versionadded:: 2.3.0

    :param value: The value to convert into a tuple
    """
    return (value, )


def convert_string_to_tuple(value):
    """THis function converts a value to a tuple if in string format.

    .. versionadded:: 2.3.0

    :param value: The potential string to convert
    :returns: The tuple (if original value was in string format) or the original value/type
    """
    if type(value) == str:
        value = convert_single_value_to_tuple(value)
    return value


def get_random_string(length=32, prefix_string=""):
    """This function returns a random alphanumeric string to use as a salt or password.

    :param length: The length of the string (``32`` by default)
    :type length: int
    :param prefix_string: A string to which the salt should be appended (optional)
    :type prefix_string: str
    :returns: The alphanumeric string
    """
    return f"{prefix_string}{''.join([random.choice(string.ascii_letters + string.digits) for _ in range(length)])}"


def display_warning(warn_msg):
    """This function displays a :py:exc:`UserWarning` message via the :py:mod:`warnings` module.

    .. versionadded:: 2.1.0

    :param warn_msg: The message to be displayed
    :type warn_msg: str
    :returns: None
    """
    warnings.warn(warn_msg, UserWarning)
    return


def get_file_type(file_path):
    """This function attempts to identify if a given file path is for a YAML or JSON file.

    .. versionadded:: 2.2.0

    :param file_path: The full path to the file
    :type file_path: str
    :returns: The file type in string format (e.g. ``yaml`` or ``json``)
    :raises: :py:exc:`FileNotFoundError`, :py:exc:`khoros.errors.exceptions.UnknownFileTypeError`
    """
    file_type = 'unknown'
    if os.path.isfile(file_path):
        if file_path.endswith('.json'):
            file_type = 'json'
        elif file_path.endswith('.yml') or file_path.endswith('.yaml'):
            file_type = 'yaml'
        else:
            display_warning(f"Unable to recognize the file type of '{file_path}' by its extension.")
            with open(file_path) as cfg_file:
                for line in cfg_file:
                    if line.startswith('#'):
                        continue
                    else:
                        if '{' in line:
                            file_type = 'json'
                            break
        if file_type == 'unknown':
            raise errors.exceptions.UnknownFileTypeError(file=file_path)
    else:
        raise FileNotFoundError(f"Unable to locate the following file: {file_path}")
    return file_type


def convert_dict_id_values_to_strings(dict_list):
    """This function ensures that the ``id`` keys in a list of dictionaries use string values.

    :param dict_list: List (or tuple) of dictionaries (or a single dictionary) containing API object data
    :type dict_list: list, tuple, dict, None
    :returns: A new dictionary list with properly formatted ``id`` values
    :raises: :py:exc:`TypeError`
    """
    dict_list = [dict_list] if isinstance(dict_list, dict) else dict_list
    new_dict_list = []
    for single_dict in dict_list:
        if not isinstance(single_dict, dict):
            raise TypeError("The 'dict_list' argument must be a dictionary or a list of dictionaries.")
        if 'id' in single_dict and not isinstance(single_dict.get('id'), str):
            single_dict['id'] = str(single_dict.get('id'))
        new_dict_list.append(single_dict)
    return new_dict_list


def convert_list_values(values_list, convert_to='str', split_values=False, split_delimiter=','):
    """This function converts the values in a list to a different type.

    :param values_list: The list of values to be converted
    :type values_list: list, tuple, set
    :param convert_to: One of the following types: ``str`` (Default), ``int``, ``float``, ``tuple`` or ``set``
    :param split_values: Determines if the values should be split with a specific delimiter (``False`` by default)

                         .. note:: This only applies when converting to the ``tuple`` or ``set`` types.

    :type split_values: bool
    :param split_delimiter: The delimiter for which to split the values when applicable (comma by default)
    :type split_delimiter: str
    :returns: A new list of converted values
    :raises: :py:exc:`TypeError`, :py:exc:`ValueError`
    """
    new_list = []
    for value in values_list:
        if convert_to == 'str':
            new_list.append(str(value))
        elif convert_to == 'int':
            new_list.append(int(value))
        elif convert_to == 'float':
            new_list.append(float(value))
        elif convert_to == 'tuple':
            value = tuple(value.split(split_delimiter)) if split_values else (value, )
            new_list.append(value)
        elif convert_to == 'set':
            value = set(value.split(split_delimiter)) if split_values else {value}
            new_list.append(value)
    return new_list


def extract_key_values_from_dict_list(key_name, dict_list, exclude_if_present=None, convert_to_string=True):
    """This function extracts values for a specific key from a list of dictionaries.

    :param key_name: The name of the dictionary key from which to extract the value(s)
    :type key_name: str
    :param dict_list: The list of dictionaries (or single dictionary) from which to extract the value(s)
    :type dict_list: list, dict
    :param exclude_if_present: Will skip extracting the key value if this given key is also present (Optional)
    :type exclude_if_present: str, None
    :param convert_to_string: Determines if the values should be converted to string format (``True`` by default)
    :type convert_to_string: bool
    :returns: A list of values extracted from the dictionary list for the given key
    :raises: :py:exc:`TypeError`
    """
    value_list, dict_list = [], [dict_list] if isinstance(dict_list, dict) else dict_list
    for single_dict in dict_list:
        if key_name in single_dict:
            skip_dict = True if exclude_if_present and exclude_if_present in single_dict else False
            if not skip_dict:
                key_value = str(single_dict.get(key_name)) if convert_to_string else single_dict.get(key_name)
                value_list.append(key_value)
    return value_list
