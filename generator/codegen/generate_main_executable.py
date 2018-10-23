from generator.codegen.codegen import include


DUMMY_MAIN = """int main(void)
{
    return 0;
}
"""


def generate_main_executable(objects):
    code = ""
    for obj in objects:
        code += include(obj["header_filename"])
    code += "\n" + DUMMY_MAIN
    return code
