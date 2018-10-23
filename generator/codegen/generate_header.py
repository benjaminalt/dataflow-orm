from generator.codegen.cls import Class
from generator.codegen.common import AccessModifier, begin_namespace, end_namespace, include
from generator.codegen.member_object import MemberObject
from generator.utils import decapitalize
from . import boilerplate


def generate_header(obj):
    includes = set()
    # TODO: Boilerplate includes
    # Each column corresponds to a primitive member with a getter and setter
    member_objects = []
    member_functions = []
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
    header_contents += begin_namespace("dataflow")
    header_contents += cls.definition()
    header_contents += end_namespace()
    return header_contents
