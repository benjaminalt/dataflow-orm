from unittest import TestCase

from generator.codegen.common import AccessModifier
from generator.codegen.function import Function, Argument


class TestFunction(TestCase):
    def test_declaration(self):
        fn = Function("testFunction", [Argument("arg1", "std::string", True, True),
                                       Argument("arg2", "int", False, True)],
                      "bool", AccessModifier.PROTECTED, "return \"test\";", True)
        self.assertEqual("virtual bool testFunction(const std::string& arg1, const int arg2);", fn.declaration())
        purely_virtual_fn = Function("testFunction", [Argument("arg1", "std::string", True, True),
                                                   Argument("arg2", "int", False, True)],
                      "bool", AccessModifier.PROTECTED, None, True, False, False, True)
        self.assertEqual("virtual bool testFunction(const std::string& arg1, const int arg2) = 0;", purely_virtual_fn.declaration())
        const_fn = Function("testFunction", [Argument("arg1", "std::string", True, True),
                                             Argument("arg2", "int", False, True)],
                      "bool", AccessModifier.PROTECTED, "return \"test\";", True, False, True, False)
        self.assertEqual("virtual bool testFunction(const std::string& arg1, const int arg2) const;", const_fn.declaration())

    def test_definition(self):
        fn = Function("testFunction", [Argument("arg1", "std::string", True, True),
                                       Argument("arg2", "int", False, True)],
                      "bool", AccessModifier.PROTECTED, "return \"test\";", True)
        self.assertEqual("""virtual bool testFunction(const std::string& arg1, const int arg2)
{
    return "test";
};""", fn.definition())

    def test_signature(self):
        fn = Function("testFunction", [Argument("arg1", "std::string", True, True),
                                       Argument("arg2", "int", False, True)],
                      "bool", AccessModifier.PROTECTED, "return \"test\"", True)
        self.assertEqual("testFunction(const std::string& arg1, const int arg2)", fn.signature())
