from generator.codegen.common import AccessModifier
from generator.codegen.member_function import MemberFunction, Argument
from generator.mysql.data_type import VoidType
from generator.utils import capitalize


class MemberObject(object):
    def __init__(self, name, datatype, access_modifier=AccessModifier.PUBLIC, const=False):
        self.name = name
        self.variable_name = name + "_"
        self.type = datatype
        self.access_modifier = access_modifier
        self.const = const

    @staticmethod
    def has_definition():
        return False

    def declaration(self):
        return "{}{} {};".format(
            "const " if self.const else "",
            self.type.cpp_type(),
            self.variable_name)

    def getter(self):
        return MemberFunction(self.name,
                              arguments=None,
                              return_type=self.type,
                              access_modifier=AccessModifier.PUBLIC,
                              body="return {};".format(self.variable_name),
                              virtual=False,
                              static=False,
                              const=True,
                              purely_virtual=False)

    def setter(self):
        return MemberFunction("set{}".format(capitalize(self.name)),
                              arguments=[Argument("value", self.type, reference=True, const=True)],
                              return_type=VoidType(),
                              access_modifier=AccessModifier.PUBLIC,
                              body="{} = value;".format(self.variable_name),
                              virtual=False,
                              static=False,
                              const=False,
                              purely_virtual=False)

    def required_headers(self):
        return self.type.required_headers()
