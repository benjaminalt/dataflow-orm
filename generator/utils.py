import inflection

def object_name(column_name):
    return inflection.camelize(column_name.strip("`"), True)