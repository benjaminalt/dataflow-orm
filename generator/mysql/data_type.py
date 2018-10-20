import re
from enum import Enum


class MySqlTypeCategories(Enum):
    INTEGRAL = 1
    FLOATING_POINT = 2
    DATETIME = 3
    STRING = 4


class MySqlBaseType(object):
    def __init__(self, mysql_type_regex, cpp_string, category):
        self.mysql_type_regex = re.compile(mysql_type_regex)
        self.cpp_string = cpp_string
        self.category = category


MYSQL_BASE_TYPES = [
    MySqlBaseType("INT", "int32_t", MySqlTypeCategories.INTEGRAL),
    MySqlBaseType("TINYINT", "int8_t", MySqlTypeCategories.INTEGRAL),
    MySqlBaseType("SMALLINT", "int16_t", MySqlTypeCategories.INTEGRAL),
    MySqlBaseType("MEDIUMINT", "int32_t", MySqlTypeCategories.INTEGRAL),
    MySqlBaseType("BIGINT", "int64_t", MySqlTypeCategories.INTEGRAL),

    MySqlBaseType("FLOAT(\([0-9]+,[0-9]+\))?", "float", MySqlTypeCategories.FLOATING_POINT),
    MySqlBaseType("DOUBLE(\([0-9]+,[0-9]+\))?", "double", MySqlTypeCategories.FLOATING_POINT),
    MySqlBaseType("DECIMAL(\([0-9]+,[0-9]+\))?", "double", MySqlTypeCategories.FLOATING_POINT),
    MySqlBaseType("NUMERIC(\([0-9]+,[0-9]+\))?", "double", MySqlTypeCategories.FLOATING_POINT),

    MySqlBaseType("DATE", "boost::gregorian::date", MySqlTypeCategories.DATETIME),
    MySqlBaseType("DATETIME", "boost::posix_time::ptime", MySqlTypeCategories.DATETIME),
    MySqlBaseType("TIMESTAMP", "boost::posix_time::ptime", MySqlTypeCategories.DATETIME),
    MySqlBaseType("TIME", "std::string", MySqlTypeCategories.DATETIME),
    MySqlBaseType("YEAR(\([0-9]+\))?", "uint16_t", MySqlTypeCategories.DATETIME),

    MySqlBaseType("CHAR(\([0-9]+\))?", "std::string", MySqlTypeCategories.STRING),
    MySqlBaseType("VARCHAR(\([0-9]+\))?", "std::string", MySqlTypeCategories.STRING)
]


class DataType(object):
    def __init__(self, mysql_type_string, nullable=True, unsigned=False):
        self.nullable = nullable
        self.unsigned = unsigned
        self.mysql_type_string = mysql_type_string

    def cpp_type(self):
        for base_type in MYSQL_BASE_TYPES:
            if base_type.mysql_type_regex.match(self.mysql_type_string.upper()):
                cpp_type_string = base_type.cpp_string
                if base_type.category == MySqlTypeCategories.INTEGRAL and self.unsigned:
                    cpp_type_string = "u" + cpp_type_string
                if self.nullable:
                    cpp_type_string = "boost::optional<{}>".format(cpp_type_string)
                return cpp_type_string
        raise RuntimeError("DataType::_cpp_type: No cpp type for MySQL type {}".format(self.mysql_type_string.upper()))
