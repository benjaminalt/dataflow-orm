from generator.codegen.common import AccessModifier, indent


class Class(object):
    def __init__(self, name, super_classes=None, constructors=None, member_functions=None, member_objects=None):
        self.name = name
        self.super_classes = super_classes if super_classes is not None else []
        self.constructors = constructors if constructors is not None else []
        self.member_functions = member_functions if member_functions is not None else []
        self.member_objects = member_objects if member_objects is not None else []

    def declaration(self):
        return "class {};".format(self.name)

    def definition(self):
        res = "class {}".format(self.name)
        if len(self.super_classes) > 0:
            res += ": "
            for i in range(len(self.super_classes)):
                res += "public {}".format(self.super_classes[i])
                if i < len(self.super_classes) - 1:
                    res += ", "
        res += "\n{\n"
        for access_modifier in [AccessModifier.PUBLIC, AccessModifier.PROTECTED, AccessModifier.PRIVATE]:
            member_list = "{}:".format(access_modifier.name.lower())
            have_member = False
            for member in [m for m in [item for sublist in [self.member_functions, self.member_objects] for item in sublist] if m.access_modifier == access_modifier]:
                if member.has_definition():
                    member_list += "\n" + indent(member.definition())
                else:
                    member_list += "\n" + indent(member.declaration())
                have_member = True
            if have_member:
                res += member_list + "\n"
        return res + "};"

    def required_headers(self):
        headers = set()
        for obj in self.member_objects:
            headers.update(obj.required_headers())
        for fn in self.member_functions:
            headers.update(fn.required_headers())
        return headers
