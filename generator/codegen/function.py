from generator.codegen.common import AccessModifier, indent


class Argument(object):
    def __init__(self, name, type, reference=False, const=False):
        self.name = name
        self.type = type
        self.reference = reference
        self.const = const

    def __str__(self):
        return "{}{}{} {}".format(
            "const " if self.const else "",
            self.type,
            "&" if self.reference else "",
            self.name
        )


class Function(object):
    def __init__(self, name, arguments=None, return_type="void", access_modifier=AccessModifier.PUBLIC, body=None,
                 virtual=False, static=False, const = False, purely_virtual=False):
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
        return "{}{} {}{}{};".format(
            "virtual " if self.virtual else "",
            self.return_type,
            self.signature(),
            " const" if self.const else "",
            " = 0" if self.purely_virtual else ""
        )

    def definition(self):
        if self.purely_virtual:
            return self.declaration()
        res = self.declaration().rstrip(";") + "\n{\n"
        res += indent(self.body)
        return res + "\n};"

    def signature(self):
        return "{}({})".format(self.name,
                               ", ".join([str(arg) for arg in self.arguments]))
