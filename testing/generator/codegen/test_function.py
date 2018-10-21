from unittest import TestCase

from generator.codegen.common import AccessModifier
from generator.codegen.member_function import MemberFunction, Argument
from generator.mysql.data_type import CppDataType


class TestFunction(TestCase):
    def test_declaration(self):
        fn = MemberFunction("testFunction", [Argument("arg1", CppDataType("std::string", ["string"]), True, True),
                                             Argument("arg2", CppDataType("int"), False, True)],
                            CppDataType("bool"), AccessModifier.PROTECTED, "return \"test\";", True)
        self.assertEqual("virtual bool testFunction(const std::string& arg1, const int arg2);", fn.declaration())
        purely_virtual_fn = MemberFunction("testFunction", [Argument("arg1", CppDataType("std::string", ["string"]), True, True),
                                                            Argument("arg2", CppDataType("int"), False, True)],
                            CppDataType("bool"), AccessModifier.PROTECTED, None, True, False, False, True)
        self.assertEqual("virtual bool testFunction(const std::string& arg1, const int arg2) = 0;", purely_virtual_fn.declaration())
        const_fn = MemberFunction("testFunction", [Argument("arg1", CppDataType("std::string", ["string"]), True, True),
                                                   Argument("arg2", CppDataType("int"), False, True)],
                            CppDataType("bool"), AccessModifier.PROTECTED, "return \"test\";", True, False, True, False)
        self.assertEqual("virtual bool testFunction(const std::string& arg1, const int arg2) const;", const_fn.declaration())

    def test_definition(self):
        fn = MemberFunction("testFunction", [Argument("arg1", CppDataType("std::string", ["string"]), True, True),
                                             Argument("arg2", CppDataType("int"), False, True)],
                            CppDataType("bool"), AccessModifier.PROTECTED, "return \"test\";", True)
        self.assertEqual("""virtual bool testFunction(const std::string& arg1, const int arg2)
{
    return "test";
};""", fn.definition())

    def test_signature(self):
        fn = MemberFunction("testFunction", [Argument("arg1", CppDataType("std::string", ["string"]), True, True),
                                             Argument("arg2", CppDataType("int"), False, True)],
                            CppDataType("bool"), AccessModifier.PROTECTED, "return \"test\"", True)
        self.assertEqual("testFunction(const std::string& arg1, const int arg2)", fn.signature())
