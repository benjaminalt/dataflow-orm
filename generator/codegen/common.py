from enum import Enum
import re


class AccessModifier(Enum):
    PUBLIC = 1
    PROTECTED = 2
    PRIVATE = 3


def indent(text):
    return re.sub('^', ' ' * 4, text, flags=re.MULTILINE)


def begin_namespace(namespace):
    return "namespace {}\n{{\n".format(namespace)


def end_namespace():
    return "\n}\n"


def include(header):
    return "#include <{}>\n".format(header)