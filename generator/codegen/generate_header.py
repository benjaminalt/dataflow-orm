from generator.codegen.cls import Class
from generator.codegen.common import AccessModifier, begin_namespace, end_namespace, include
from generator.codegen.member_function import MemberFunction, Argument
from generator.codegen.member_object import MemberObject
from generator.mysql.data_type import CppDataType
from generator.utils import decapitalize
from . import boilerplate


def generate_header(obj, namespace="dataflow"):
    includes = set()

    # Each column corresponds to a primitive member with a getter and setter
    member_objects = []
    member_functions = [
        MemberFunction("accept",
                       [Argument("visitor", CppDataType("Visitor", ["Visitor.h"]), reference=True)],
                       body="visitor.visit(*this);", const=False),
        MemberFunction("accept",
                       [Argument("visitor", CppDataType("ConstVisitor", ["ConstVisitor.h"]), reference=True)],
                       body="visitor.visit(*this);", const=True)
    ]
    for column in obj["columns"]:
        private_member_object = MemberObject(decapitalize(column["object_name"]), column["data_type"], access_modifier=AccessModifier.PRIVATE)
        member_objects.append(private_member_object)
        member_functions.append(private_member_object.getter())
        member_functions.append(private_member_object.setter())
    cls = Class(obj["name"], super_classes=None, constructors=None,
                member_functions=member_functions, member_objects=member_objects)
    includes.update(cls.required_headers())

    header_contents = boilerplate.header_comment + "\n"
    header_contents += boilerplate.pragma + "\n"
    for header in includes:
        header_contents += include(header)
    if len(includes) > 0:
        header_contents += "\n"
    header_contents += begin_namespace(namespace)
    header_contents += cls.definition() + "\n"
    header_contents += end_namespace(namespace)
    return header_contents
