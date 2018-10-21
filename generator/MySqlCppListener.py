from generated.MySqlParser import MySqlParser
from generated.MySqlParserListener import MySqlParserListener
from generator import utils
from generator.codegen import codegen
from generator.mysql.data_type import MySqlDataType

import os


class MySqlCppListener(MySqlParserListener):
    def __init__(self, output_dir):
        self.output_dir = output_dir
        self.include_dir = os.path.join(output_dir, "include")
        self.objects = []

    def enterSqlStatements(self, ctx:MySqlParser.SqlStatementsContext):
        pass

    def exitSqlStatements(self, ctx:MySqlParser.SqlStatementsContext):
        # Add boilerplate
        # Create header for each object
        for object in self.objects:
            header_contents = codegen.generate_header(object)
            with open(os.path.join(self.include_dir, object["header_filename"]), "w") as header_file:
                header_file.write(header_contents)
        # Create visitor

    def enterColumnCreateTable(self, ctx:MySqlParser.ColumnCreateTableContext):
        # Each table corresponds to one object
        table_name = ctx.tableName().getText()
        print("MySqlCppListener::enterColumnCreateTable: {}".format(table_name))
        object_name = utils.object_name(table_name)
        object = {
            "name": object_name,
            "header_filename": object_name + ".h",
            "columns": []
        }
        self.objects.append(object)

    def enterColumnDeclaration(self, ctx:MySqlParser.ColumnDeclarationContext):
        column_name = ctx.uid().getText()
        print("MySqlCppListener::enterColumnDeclaration: {}".format(column_name))
        self.objects[-1]["columns"].append({"type": "column",
                                      "column_name": column_name,
                                      "object_name": utils.object_name(column_name)})

    def enterColumnDefinition(self, ctx:MySqlParser.ColumnDefinitionContext):
        print("MySqlCppListener::enterColumnDefinition")
        self.objects[-1]["columns"][-1]["data_type"] = MySqlDataType(ctx.dataType().getText())

    def enterNullColumnConstraint(self, ctx:MySqlParser.NullColumnConstraintContext):
        self.objects[-1]["columns"][-1]["data_type"].set_nullable(
            not (ctx.nullNotnull().NOT() is not None and ctx.nullNotnull().NULL_LITERAL() is not None))

    def enterDimensionDataType(self, ctx:MySqlParser.DimensionDataTypeContext):
        self.objects[-1]["columns"][-1]["data_type"].set_unsigned(ctx.UNSIGNED() is not None)
