from generated.MySqlParser import MySqlParser
from generated.MySqlParserVisitor import MySqlParserVisitor
import os


class MySqlCppVisitor(MySqlParserVisitor):
    def __init__(self, output_dir):
        self.output_dir = output_dir
        self.include_dir = os.path.join(output_dir, "include")

    def visitSqlStatements(self, ctx:MySqlParser.SqlStatementsContext):
        print("MySqlCppVisitor::visitSqlStatements")
        for child in ctx.children:
            child.accept(self)

    def visitDdlStatement(self, ctx:MySqlParser.DdlStatementContext):
        print("MySqlCppVisitor::visitDdlStatement")
        print("children: {}", ctx.children)
        for child in ctx.children:
            child.accept(self)

    def visitColumnCreateTable(self, ctx:MySqlParser.ColumnCreateTableContext):
        print("MySqlCppVisitor::visitColumnCreateTable: {}".format(ctx.tableName().getText()))