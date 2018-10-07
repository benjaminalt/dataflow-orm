CMAKELISTS_TEMPLATE = """cmake_minimum_required(VERSION {})
project({})
{}
{}
{}"""

CMAKE_MINIMUM_VERSION = "2.8.9"
CMAKE_PACKAGES = {"Boost": "Boost_INCLUDE_DIRS"}
EXECUTABLES = {"test": ["main.cpp"]}

def generate_find_package():
    res = ""
    for package_name in CMAKE_PACKAGES.keys():
        res += "find_package({} REQUIRED)\n".format(package_name)
    return res


def generate_include_directories():
    res = "include_directories(\n    include\n"
    for package_include_dir_variable in CMAKE_PACKAGES.values():
        res += "    ${{{}}}\n".format(package_include_dir_variable)
    res += ")"
    return res


def generate_executables():
    res = ""
    for executable_name, sources in EXECUTABLES.items():
        res += "add_executable({} {})\n".format(executable_name, " ".join(sources))
    return res


def generate_cmakelists(project_name):
    return CMAKELISTS_TEMPLATE.format(CMAKE_MINIMUM_VERSION,
                                      project_name,
                                      generate_find_package(),
                                      generate_include_directories(),
                                      generate_executables())