from unittest import TestCase

from generator.mysql.data_type import DataType


class TestDataType(TestCase):
    def test__cpp_type(self):
        self.assertEqual(DataType("varchar(255)", nullable=False, unsigned=False).cpp_type_string, "std::string")
        self.assertEqual(DataType("varchar", nullable=False, unsigned=True).cpp_type_string, "std::string")
        self.assertEqual(DataType("VARCHAR(16)", nullable=False).cpp_type_string, "std::string")
        self.assertEqual(DataType("int", nullable=True, unsigned=False).cpp_type_string, "boost::optional<int32_t>")
        self.assertEqual(DataType("int", nullable=False, unsigned=False).cpp_type_string, "int32_t")
        self.assertEqual(DataType("int", nullable=False, unsigned=True).cpp_type_string, "uint32_t")
        self.assertEqual(DataType("int", nullable=True, unsigned=True).cpp_type_string, "boost::optional<uint32_t>")
        self.assertEqual(DataType("double(16,4)", nullable=False, unsigned=True).cpp_type_string, "double")
        self.assertEqual(DataType("DOUBLE(16,4", nullable=False, unsigned=False).cpp_type_string, "double")