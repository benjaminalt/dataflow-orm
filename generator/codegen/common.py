from enum import Enum
import re


class AccessModifier(Enum):
    PUBLIC = 1
    PROTECTED = 2
    PRIVATE = 3


def indent(text):
    return re.sub('^', ' ' * 4, text, flags=re.MULTILINE)


def begin_namespace(namespace):
    namespaces = namespace.split("::")
    res = ""
    for ns in namespaces:
        res += "namespace {}\n{{\n".format(ns)
    return res


def end_namespace(namespace):
    namespaces = namespace.split("::")
    res = ""
    for ns in namespaces:
        res += "}\n"
    return res


def include(header):
    return "#include <{}>\n".format(header)