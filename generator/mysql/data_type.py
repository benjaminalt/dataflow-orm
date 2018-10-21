import re
from enum import Enum
from abc import ABC, abstractmethod

OPTIONAL_HEADER = "boost/optional.hpp"
OPTIONAL_TEMPLATE_TYPE = "boost::optional"
INT_HEADER = "stdint.h"
STRING_HEADER = "string"
DATE_HEADER = "boost/date_time/gregorian/gregorian.hpp"
DATETIME_HEADER = "boost/date_time/posix_time/posix_time.hpp"


class MySqlTypeCategories(Enum):
    INTEGRAL = 1
    FLOATING_POINT = 2
    DATETIME = 3
    STRING = 4


class MySqlBaseType(object):
    def __init__(self, mysql_type_regex, cpp_string, category, header=None):
        self.mysql_type_regex = re.compile(mysql_type_regex)
        self.cpp_string = cpp_string
        self.category = category
        self.header = header


MYSQL_BASE_TYPES = [
    MySqlBaseType("INT", "int32_t", MySqlTypeCategories.INTEGRAL, INT_HEADER),
    MySqlBaseType("TINYINT", "int8_t", MySqlTypeCategories.INTEGRAL, INT_HEADER),
    MySqlBaseType("SMALLINT", "int16_t", MySqlTypeCategories.INTEGRAL, INT_HEADER),
    MySqlBaseType("MEDIUMINT", "int32_t", MySqlTypeCategories.INTEGRAL, INT_HEADER),
    MySqlBaseType("BIGINT", "int64_t", MySqlTypeCategories.INTEGRAL, INT_HEADER),

    MySqlBaseType("FLOAT(\([0-9]+,[0-9]+\))?", "float", MySqlTypeCategories.FLOATING_POINT),
    MySqlBaseType("DOUBLE(\([0-9]+,[0-9]+\))?", "double", MySqlTypeCategories.FLOATING_POINT),
    MySqlBaseType("DECIMAL(\([0-9]+,[0-9]+\))?", "double", MySqlTypeCategories.FLOATING_POINT),
    MySqlBaseType("NUMERIC(\([0-9]+,[0-9]+\))?", "double", MySqlTypeCategories.FLOATING_POINT),

    MySqlBaseType("DATE", "boost::gregorian::date", MySqlTypeCategories.DATETIME, DATE_HEADER),
    MySqlBaseType("DATETIME", "boost::posix_time::ptime", MySqlTypeCategories.DATETIME, DATETIME_HEADER),
    MySqlBaseType("TIMESTAMP", "boost::posix_time::ptime", MySqlTypeCategories.DATETIME, DATETIME_HEADER),
    MySqlBaseType("TIME", "std::string", MySqlTypeCategories.DATETIME, STRING_HEADER),
    MySqlBaseType("YEAR(\([0-9]+\))?", "uint16_t", MySqlTypeCategories.DATETIME, INT_HEADER),

    MySqlBaseType("CHAR(\([0-9]+\))?", "std::string", MySqlTypeCategories.STRING, STRING_HEADER),
    MySqlBaseType("VARCHAR(\([0-9]+\))?", "std::string", MySqlTypeCategories.STRING, STRING_HEADER)
]


class DataType(ABC):
    @abstractmethod
    def cpp_type(self):
        pass

    @abstractmethod
    def required_headers(self):
        pass


class MySqlDataType(DataType):
    def __init__(self, mysql_type_string, nullable=True, unsigned=False):
        self._nullable = nullable
        self._unsigned = unsigned
        self._base_type = self._mysql_base_type(mysql_type_string)

    def set_nullable(self, nullable):
        self._nullable = nullable

    def set_unsigned(self, unsigned):
        self._unsigned = unsigned

    def cpp_type(self):
        cpp_type_string = self._base_type.cpp_string
        if self._base_type.category == MySqlTypeCategories.INTEGRAL and self._unsigned:
            cpp_type_string = "u" + cpp_type_string
        if self._nullable:
            cpp_type_string = "{}<{}>".format(OPTIONAL_TEMPLATE_TYPE, cpp_type_string)
        return cpp_type_string

    def required_headers(self):
        headers = [self._base_type.header] if self._base_type.header is not None else []
        if self._nullable:
            headers.append(OPTIONAL_HEADER)
        return headers

    @staticmethod
    def _mysql_base_type(mysql_type_string):
        for base_type in MYSQL_BASE_TYPES:
            if base_type.mysql_type_regex.match(mysql_type_string.upper()):
                return base_type
        raise RuntimeError("MySqlDataType::_mysql_base_type: No cpp type for MySQL type {}".format(mysql_type_string.upper()))


class CppDataType(DataType):
    def __init__(self, cpp_type_string, headers=None):
        self.cpp_type_string = cpp_type_string
        self.headers = headers if headers is not None else []

    def cpp_type(self):
        return self.cpp_type_string

    def required_headers(self):
        return self.headers


class VoidType(DataType):
    def cpp_type(self):
        return "void"

    def required_headers(self):
        return []
