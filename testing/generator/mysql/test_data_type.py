from unittest import TestCase

from generator.mysql.data_type import DataType, MySqlDataType


class TestMySqlDataType(TestCase):
    def test_cpp_type(self):
        self.assertEqual(MySqlDataType("varchar(255)", nullable=False, unsigned=False).cpp_type(), "std::string")
        self.assertEqual(MySqlDataType("varchar", nullable=False, unsigned=True).cpp_type(), "std::string")
        self.assertEqual(MySqlDataType("VARCHAR(16)", nullable=False).cpp_type(), "std::string")
        self.assertEqual(MySqlDataType("int", nullable=True, unsigned=False).cpp_type(), "boost::optional<int32_t>")
        self.assertEqual(MySqlDataType("int", nullable=False, unsigned=False).cpp_type(), "int32_t")
        self.assertEqual(MySqlDataType("int", nullable=False, unsigned=True).cpp_type(), "uint32_t")
        self.assertEqual(MySqlDataType("int", nullable=True, unsigned=True).cpp_type(), "boost::optional<uint32_t>")
        self.assertEqual(MySqlDataType("double(16,4)", nullable=False, unsigned=True).cpp_type(), "double")
        self.assertEqual(MySqlDataType("DOUBLE(16,4", nullable=False, unsigned=False).cpp_type(), "double")
