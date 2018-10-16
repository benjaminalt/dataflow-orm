from enum import Enum
import re


class AccessModifier(Enum):
    PUBLIC = 1
    PROTECTED = 2
    PRIVATE = 3


def indent(text):
    return re.sub('^', ' ' * 4, text, flags=re.MULTILINE)