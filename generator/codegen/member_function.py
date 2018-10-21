from generator.codegen.common import AccessModifier, indent
from generator.mysql.data_type import VoidType


class Argument(object):
    def __init__(self, name, datatype, reference=False, const=False):
        self.name = name
        self.type = datatype
        self.reference = reference
        self.const = const

    def __str__(self):
        return "{}{}{} {}".format(
            "const " if self.const else "",
            self.type.cpp_type(),
            "&" if self.reference else "",
            self.name)

    def required_headers(self):
        return self.type.required_headers()


class MemberFunction(object):
    def __init__(self, name, arguments=None, return_type=VoidType(), access_modifier=AccessModifier.PUBLIC, body=None,
                 virtual=False, static=False, const=False, purely_virtual=False):
        if static and (const or virtual or purely_virtual):
            raise ValueError("Illegal argument: Function cannot be both static and either const or virtual")
        if purely_virtual and not virtual:
            raise ValueError("Illegal argument: Purely virtual function must also be virtual")
        if purely_virtual and (body is not None):
            raise ValueError("Illegal argument: Purely virtual function cannot have a body")
        self.name = name
        self.arguments = arguments if arguments is not None else []
        self.return_type = return_type
        self.access_modifier = access_modifier
        self.body = body
        self.const = const
        self.static = static
        self.virtual = virtual
        self.purely_virtual = purely_virtual

    def declaration(self):
        modifier = ""
        if self.static:
            modifier = "static "
        elif self.virtual:
            modifier = "virtual "
        return "{}{} {}{}{};".format(
            modifier,
            self.return_type.cpp_type(),
            self.signature(),
            " const" if self.const else "",
            " = 0" if self.purely_virtual else ""
        )

    def definition(self):
        if not self.has_definition():
            raise ValueError("Cannot create a function definition without a body")
        res = self.declaration().rstrip(";") + "\n{\n"
        res += indent(self.body)
        return res + "\n};"

    def has_definition(self):
        return not self.purely_virtual and self.body is not None

    def signature(self):
        return "{}({})".format(self.name,
                               ", ".join([str(arg) for arg in self.arguments]))

    def required_headers(self):
        headers = set()
        for arg in self.arguments:
            headers.update(arg.required_headers())
        headers.update(self.return_type.required_headers())
        return headers
