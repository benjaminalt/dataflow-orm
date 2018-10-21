import inflection


def object_name(column_name):
    return inflection.camelize(column_name.strip("`"), True)


def decapitalize(string):
    return string[:1].lower() + string[1:] if string else ''


def capitalize(string):
    return string[0].upper() + string[1:]
