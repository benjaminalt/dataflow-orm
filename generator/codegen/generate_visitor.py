from generator import utils
from generator.codegen import boilerplate, common
from generator.codegen.cls import Class
from generator.codegen.member_function import MemberFunction, Argument
from generator.mysql.data_type import CppDataType


def generate_visitor(objects, namespace="dataflow", const=False):
    header = boilerplate.header_comment + "\n"
    header += boilerplate.pragma + "\n"
    header += common.begin_namespace(namespace)
    forward_declarations = []
    visit_functions = []
    for obj in objects:
        # One visit(...) function for each object
        forward_declarations.append("class {};\n".format(obj["name"]))
        visit_functions.append(MemberFunction(
            "visit",
            arguments=[Argument(utils.decapitalize(obj["name"]),
                                CppDataType(utils.capitalize(obj["name"])),
                                reference=True, const=const)],
            virtual=True, purely_virtual=True))
    visitor = Class(
        "{}Visitor".format("Const" if const else ""),
        member_functions=visit_functions)
    for forward_declaration in forward_declarations:
        header += forward_declaration
    header += visitor.definition() + "\n"
    header += common.end_namespace(namespace)
    return header
