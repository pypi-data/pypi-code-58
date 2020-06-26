import re
import textwrap
from ast import parse as ast_parse
from pathlib import Path
from typing import Optional, Union

import black
import toml

from snakefmt import DEFAULT_LINE_LENGTH
from snakefmt.exceptions import (
    InvalidPython,
    InvalidParameterSyntax,
    InvalidBlackConfiguration,
    MalformattedToml,
)
from snakefmt.parser.grammar import SnakeRule
from snakefmt.parser.parser import Parser
from snakefmt.parser.syntax import (
    Parameter,
    ParameterSyntax,
    SingleParam,
    RuleInlineSingleParam,
    TAB,
)
from snakefmt.types import TokenIterator

PathLike = Union[Path, str]
rule_like_formatted = {"rule", "checkpoint"}

triple_quote_matcher = re.compile(r"(\"{3}.*?\"{3})|('{3}.*?'{3})", re.DOTALL)
contextual_matcher = re.compile(
    r"(.*)^(if|elif|else|with|for|while)(.*)(:.*)", re.S | re.M
)


class Formatter(Parser):
    def __init__(
        self,
        snakefile: TokenIterator,
        line_length: int = DEFAULT_LINE_LENGTH,
        black_config: Optional[PathLike] = None,
    ):
        self._line_length: int = line_length
        self.result: str = ""
        self.lagging_comments: str = ""
        self.no_formatting_yet: bool = True

        if black_config is None:
            self.black_mode = black.FileMode(line_length=self.line_length)
        else:
            self.black_mode = self.read_black_config(black_config)

        super().__init__(snakefile)  # Call to parse snakefile

    def read_black_config(self, path: PathLike) -> black.FileMode:
        if not Path(path).is_file():
            raise FileNotFoundError(f"{path} is not a file.")

        try:
            pyproject_toml = toml.load(path)
            config = pyproject_toml.get("tool", {}).get("black", {})
        except toml.TomlDecodeError as error:
            raise MalformattedToml(error)

        if "line_length" not in config:
            config["line_length"] = self.line_length

        try:
            return black.FileMode(**config)
        except TypeError as error:
            raise InvalidBlackConfiguration(error)

    @property
    def line_length(self) -> int:
        return self._line_length

    def get_formatted(self) -> str:
        return self.result

    def flush_buffer(
        self,
        from_python: bool = False,
        final_flush: bool = False,
        in_global_context: bool = False,
    ) -> None:
        if len(self.buffer) == 0 or self.buffer.isspace():
            self.result += self.buffer
            self.buffer = ""
            return

        if not from_python:
            formatted = self.run_black_format_str(self.buffer)
            if self.target_indent > 0:
                formatted = self.align_strings(formatted, self.target_indent)
        else:
            # Invalid python syntax, eg lone 'else:' between two rules, can occur.
            # Below constructs valid code statements and formats them.
            re_match = contextual_matcher.match(self.buffer)
            if re_match is not None:
                callback_keyword = re_match.group(2)
                used_keyword = (
                    "if" if callback_keyword in {"elif", "else"} else callback_keyword
                )
                condition = re_match.group(3)
                if condition != "":
                    test_substitute = f"{used_keyword}{condition}"
                else:
                    test_substitute = f"{used_keyword} a"
                to_format = (
                    f"{re_match.group(1)}{test_substitute}"
                    f"{re_match.group(4)}"
                    f"{TAB * self.context.cur_indent}pass"
                )
                formatted = self.run_black_format_str(to_format)
                re_rematch = contextual_matcher.match(formatted)
                if condition != "":
                    callback_keyword += re_rematch.group(3)
                formatted = (
                    f"{re_rematch.group(1)}{callback_keyword}" f"{re_rematch.group(4)}"
                )
                formatted_lines = formatted.splitlines(keepends=True)
                formatted = "".join(formatted_lines[:-1])  # Remove the 'pass' line
            else:
                formatted = self.run_black_format_str(self.buffer)

        # Re-add newline removed by black for proper parsing of comments
        if self.buffer.endswith("\n\n"):
            formatted += "\n"
        self.add_newlines(self.target_indent, formatted, final_flush, in_global_context)
        self.buffer = ""

    def process_keyword_context(self, in_global_context: bool):
        cur_indent = self.context.cur_indent
        self.add_newlines(cur_indent, in_global_context=in_global_context)
        formatted = (
            f"{TAB * cur_indent}{self.context.keyword_name}:{self.context.comment}\n"
        )
        self.result += formatted

    def process_keyword_param(
        self, param_context: ParameterSyntax, in_global_context: bool
    ):
        self.add_newlines(
            param_context.target_indent - 1, in_global_context=in_global_context
        )
        in_rule = issubclass(param_context.incident_vocab.__class__, SnakeRule)
        self.result += self.format_params(param_context, in_rule)

    def run_black_format_str(self, string: str) -> str:
        try:
            fmted = black.format_str(string, mode=self.black_mode)
        except black.InvalidInput as e:
            raise InvalidPython(
                f"Got error:\n```\n{str(e)}\n```\n" f"while formatting code with black."
            ) from None
        return fmted

    def align_strings(self, string: str, target_indent: int) -> str:
        """
        Takes an ensemble of strings and indents/reindents it
        """
        pos = 0
        used_indent = TAB * target_indent
        indented = ""
        for match in re.finditer(triple_quote_matcher, string):
            indented += textwrap.indent(string[pos : match.start()], used_indent)
            match_slice = string[match.start() : match.end()].replace("\t", TAB)
            if match_slice.count("\n") > 1 and target_indent > 0:
                all_lines = match_slice.splitlines(keepends=True)
                first = textwrap.indent(textwrap.dedent(all_lines[0]), used_indent)
                last = textwrap.indent(textwrap.dedent(all_lines[-1]), used_indent)
                middle = textwrap.indent(
                    textwrap.dedent("".join(all_lines[1:-1])), used_indent
                )
                indented += f"{first}{middle}{last}"
            else:
                indented += f"{used_indent}{match_slice}"
            pos = match.end()
        indented += textwrap.indent(string[pos:], used_indent)

        return indented

    def format_param(
        self,
        parameter: Parameter,
        target_indent: int,
        inline_formatting: bool,
        single_param: bool = False,
    ) -> str:
        if inline_formatting:
            target_indent = 0
        comments = f"\n{TAB * target_indent}".join(parameter.comments)
        val = str(parameter)

        try:
            # A snakemake parameter is syntactically like a function parameter
            ast_parse(f"param({val})")
        except SyntaxError:
            raise InvalidParameterSyntax(f"{parameter.line_nb}{val}") from None

        if inline_formatting:
            val = val.replace("\n", "")  # collapse strings on multiple lines
        try:
            val = self.run_black_format_str(val)
        except InvalidPython:
            if "**" in val:
                val = val.replace("** ", "**")

        val = self.align_strings(val, target_indent)
        if parameter.has_a_key():  # Remove space either side of '='
            match_equal = re.match("(.*?) = (.*)", val, re.DOTALL)
            val = f"{match_equal.group(1)}={match_equal.group(2)}"

        val = val.strip("\n")
        if single_param:
            result = f"{val}{comments}\n"
        else:
            result = f"{val},{comments}\n"
        return result

    def format_params(self, parameters: ParameterSyntax, in_rule: bool) -> str:
        target_indent = parameters.target_indent
        used_indent = TAB * (target_indent - 1)
        result = f"{used_indent}{parameters.keyword_name}:{parameters.comment}"

        p_class = parameters.__class__
        single_param = issubclass(p_class, SingleParam)
        inline_fmting = single_param
        # Cancel single param formatting if in rule-like context and param not inline
        if in_rule and p_class is not RuleInlineSingleParam:
            inline_fmting = False

        if inline_fmting:
            result += " "
        else:
            result += "\n"

        for elem in parameters.all_params:
            result += self.format_param(
                elem, target_indent, inline_fmting, single_param
            )
        return result

    def add_newlines(
        self,
        cur_indent: int,
        formatted_string: str = "",
        final_flush: bool = False,
        in_global_context: bool = False,
    ):
        """
        Top-level (indent of 0) rules and python code get two newlines separation
        Indented rules/pycode get one newline separation
        Comments immediately preceding rules/pycode get newlined with them
        """
        comment_matches = 0
        comment_break = 1
        all_lines = formatted_string.splitlines()
        if len(all_lines) > 0:
            for line in reversed(all_lines):
                if len(line) == 0 or line.lstrip()[0] != "#":
                    break
                comment_matches += 1
            comment_break = len(all_lines) - comment_matches

        if comment_break > 0 or final_flush:
            # Only add leading lines if we do not only have comments
            if not self.no_formatting_yet:
                if cur_indent == 0:
                    self.result += "\n\n"
                elif in_global_context:
                    self.result += "\n"
        if in_global_context:
            if self.lagging_comments != "":
                self.result += self.lagging_comments
                self.lagging_comments = ""

            if len(all_lines) > 0:
                if comment_break > 0:
                    self.result += "\n".join(all_lines[:comment_break]).rstrip() + "\n"
                if comment_matches > 0:
                    self.lagging_comments = "\n".join(all_lines[comment_break:]) + "\n"
                    if final_flush:
                        self.result += self.lagging_comments
        else:
            self.result += formatted_string

        if self.no_formatting_yet:
            if comment_break > 0:
                self.no_formatting_yet = False
