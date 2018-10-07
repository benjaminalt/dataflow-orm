import argparse
import os, shutil
from antlr4 import *
from generated.MySqlLexer import MySqlLexer
from generated.MySqlParser import MySqlParser
from generator.CaseChangingInputStream import CaseChangingInputStream
from generator.MySqlCppListener import MySqlCppListener
from generator.codegen.generate_cmake import generate_cmakelists


def generate(project_name, input_string, output_dir):
    include_dir = os.path.join(output_dir, "include")

    # Copy predefined headers to include dir
    script_dir = os.path.dirname(os.path.realpath(__file__))
    predefined_header_dir = os.path.join(script_dir, "codegen", "predefined")
    for predefined_header in os.listdir(predefined_header_dir):
        shutil.copyfile(os.path.join(predefined_header_dir, predefined_header), include_dir)

    # Generate headers
    input_stream = CaseChangingInputStream(input_string, InputStream(input_string), True)
    lexer = MySqlLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = MySqlParser(stream)
    tree = parser.sqlStatement()
    cpp = MySqlCppListener(output_dir)
    walker = ParseTreeWalker()
    walker.walk(cpp, tree)

    # Generate CMakeLists
    with open(os.path.join(output_dir, "CMakeLists.txt"), "w") as cmakelists_file:
        cmakelists_file.write(generate_cmakelists(project_name))


def main(args):
    print("Parsing {}...".format(args.file))
    if not (os.path.exists(args.file) and os.path.isfile(args.file)):
        raise ValueError("Input file not found: {}".format(args.file))
    with open(args.file, "r") as infile:
        file_contents = infile.read()
    output_dir = os.getcwd()
    if args.output is not None:
        if not os.path.exists(args.output):
            os.makedirs(args.output)
        if not os.path.exists(args.output) or not os.path.isdir(args.output):
            raise ValueError("Invalid output directory: {}".format(args.output))
        output_dir = args.output
    generate(args.project_name, file_contents, output_dir)


if __name__ == '__main__':
    arg_parser = argparse.ArgumentParser(description="Generate C++ data objects from MySQL CREATE TABLE statements")
    arg_parser.add_argument("project_name", type=str, help="Project name")
    arg_parser.add_argument("file", type=str, help="Path to input SQL file")
    arg_parser.add_argument("--output", type=str, help="Path to output directory (for generated header files)")
    main(arg_parser.parse_args())