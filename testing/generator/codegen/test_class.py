from unittest import TestCase
from generator.codegen.cls import Class
from generator.codegen.common import AccessModifier
from generator.codegen.member_function import MemberFunction, Argument
from generator.mysql.data_type import CppDataType, VoidType

classA = Class("ClassA", None, None, [
    MemberFunction("functionA", [Argument("a", CppDataType("std::string", ["string"]), True, True),
                                 Argument("b", CppDataType("double"), False, False)]),
    MemberFunction("functionB", None, CppDataType("bool"), AccessModifier.PROTECTED, "functionA(\"test\", 1);\nreturn true;", virtual=True),
    MemberFunction("functionC", None, CppDataType("int"), AccessModifier.PRIVATE, None, virtual=True, purely_virtual=True),
    MemberFunction("functionD", None, VoidType(), AccessModifier.PRIVATE, static=True)
], None)


class TestClass(TestCase):
    def test_declaration(self):
        self.assertEqual("class ClassA;", classA.declaration())

    def test_definition(self):
        self.assertEqual("""class ClassA
{
public:
    void functionA(const std::string& a, double b);
protected:
    virtual bool functionB()
    {
        functionA("test", 1);
        return true;
    };
private:
    virtual int functionC() = 0;
    static void functionD();
};""", classA.definition())
