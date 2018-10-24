import argparse
import os, shutil
from antlr4 import *
from generated.MySqlLexer import MySqlLexer
from generated.MySqlParser import MySqlParser
from generator.MySqlCppListener import MySqlCppListener
from generator.case_changing_input_stream import CaseChangingInputStream
from generator.codegen import generate_header
from generator.codegen.generate_cmake import generate_cmakelists
from generator.codegen.generate_main_executable import generate_main_executable


def generate(project_name, input_filepath, output_dir, namespace="dataflow"):
    include_dir = os.path.join(output_dir, "include")
    if not os.path.exists(include_dir):
        os.makedirs(include_dir)
    # Copy predefined headers to include dir
    script_dir = os.path.dirname(os.path.realpath(__file__))
    predefined_header_dir = os.path.join(script_dir, "codegen", "predefined")
    for predefined_header in os.listdir(predefined_header_dir):
        shutil.copy(os.path.join(predefined_header_dir, predefined_header), include_dir)

    # Generate headers
    with open(input_filepath, "r") as infile:
        file_contents = infile.read()
    input_stream = CaseChangingInputStream(file_contents, InputStream(file_contents), True)
    lexer = MySqlLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = MySqlParser(stream)
    tree = parser.sqlStatements()
    listener = MySqlCppListener()
    walker = ParseTreeWalker()
    walker.walk(listener, tree)

    # Add boilerplate
    # TODO
    # Create header for each object
    for obj in listener.objects:
        header_contents = generate_header.generate_header(obj, namespace)
        with open(os.path.join(include_dir, obj["header_filename"]), "w") as header_file:
            header_file.write(header_contents)
    # Create visitor

    # Dummy executable
    with open(os.path.join(output_dir, "main.cpp"), "w") as dummy_executable:
        dummy_executable.write(generate_main_executable(listener.objects))
    # Generate CMakeLists
    with open(os.path.join(output_dir, "CMakeLists.txt"), "w") as cmakelists_file:
        cmakelists_file.write(generate_cmakelists(project_name))


def main(args):
    print("Parsing {}...".format(args.file))
    if not (os.path.exists(args.file) and os.path.isfile(args.file)):
        raise ValueError("Input file not found: {}".format(args.file))
    output_dir = os.getcwd()
    if args.output is not None:
        if not os.path.exists(args.output):
            os.makedirs(args.output)
        if not os.path.exists(args.output) or not os.path.isdir(args.output):
            raise ValueError("Invalid output directory: {}".format(args.output))
        output_dir = args.output
    namespace = args.namespace if args.namespace is not None else "dataflow"
    generate(args.project_name, args.file, output_dir, namespace)


if __name__ == '__main__':
    arg_parser = argparse.ArgumentParser(description="Generate C++ data objects from MySQL CREATE TABLE statements")
    arg_parser.add_argument("project_name", type=str, help="Project name")
    arg_parser.add_argument("file", type=str, help="Path to input SQL file")
    arg_parser.add_argument("--output", type=str, help="Path to output directory (for generated header files)")
    arg_parser.add_argument("--namespace", type=str, help="Custom namespace (default is dataflow)")
    main(arg_parser.parse_args())