from unittest import TestCase
from generator.codegen.cls import Class
from generator.codegen.common import AccessModifier
from generator.codegen.function import Function, Argument

classA = Class("ClassA", None, None, [
    Function("functionA", [Argument("a", "std::string", True, True),
                           Argument("b", "double", False, False)]),
    Function("functionB", None, "bool", AccessModifier.PROTECTED, "functionA(\"test\", 1);\nreturn true;", virtual=True),
    Function("functionC", None, "int", AccessModifier.PRIVATE, None, virtual=True, purely_virtual=True),
    Function("functionD", None, "void", AccessModifier.PRIVATE, static=True)
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
