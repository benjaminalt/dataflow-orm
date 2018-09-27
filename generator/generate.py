import argparse
import os
from antlr4 import *
from generated.MySqlLexer import MySqlLexer
from generated.MySqlParser import MySqlParser
from generator.MySqlCppListener import MySqlCppListener

class CaseChangingInputStream(InputStream):
    pass

def main(args):
    print("Parsing {}...".format(args.file))
    if not (os.path.exists(args.file) and os.path.isfile(args.file)):
        raise ValueError("Input file not found: {}".format(args.file))
    with open(args.file, "r") as infile:
        file_contents = infile.read().upper()
    lexer = MySqlLexer(InputStream(file_contents))
    test = .
    stream = CommonTokenStream(lexer)
    parser = MySqlParser(stream)
    tree = parser.sqlStatement()
    output = open("test.h", "w")
    cpp = MySqlCppListener(output)
    walker = ParseTreeWalker()
    walker.walk(cpp, tree)
    output.close()
    print("Done.")


if __name__ == '__main__':
    arg_parser = argparse.ArgumentParser(description="Generate C++ data objects from MySQL CREATE TABLE statements")
    arg_parser.add_argument("file", type=str, help="Path to input SQL file")
    main(arg_parser.parse_args())