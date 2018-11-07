# dataflow-orm

A flexible, lightweight ORM for C++.

Currently supports automatic generation of header-only, visitable C++ objects from SQL CREATE statements as well as abstract
visitor classes for operating on the generated objects.

Unlike other C++ ORM solutions such as [ODB](https://www.codesynthesis.com/products/odb/) or [hiberlite](https://github.com/paulftw/hiberlite),
this solution does not make any assumptions about the concrete sources or sinks of the data, but allows the user to implement
custom visitors for instantiating and persisting objects from/to databases, REST APIs, OPC UA servers etc.

## Installation

### MySQL lexer & parser

Download and install the [ANTLR4 tool](https://github.com/antlr/antlr4/blob/master/doc/getting-started.md) and install
the [Python runtime](https://github.com/antlr/antlr4/blob/master/doc/python-target.md).

Clone this repo and install the ANTLR grammar submodule:
```
cd dataflow-orm
git submodule init && git submodule update
```

Run the ANTLR tool on the MySQL grammar to create a lexer and parser:
```
cd dataflow-orm
mkdir generated
cd dependencies/grammars-v4/mysql
antlr4 -o ../../../generated -Dlanguage=Python3 MySqlLexer.g4 MySqlParser.g4
```
This generates MySqlLexer.py, MySqlParser.py and a number of auxiliary files which are required to parse MySQL DDL statements.

### Python dependencies

Install all required Python packages:
```
pip3 install inflection ddt 
```

## Usage

`generate.py` takes a file containing SQL `CREATE TABLE` statements (and any other valid SQL, which is ignored) and creates a
header-only C++ object hierarchy from the relational objects, abstract visitor classes as well as a CMakeLists.txt for testing:
```
cd dataflow-orm
mkdir -p /path/to/output_dir
python3 generator/generate.py project_name /path/to/ddl.sql --output /path/to/output_dir
```
The optional argument `--output` specifies an output directory. If none is given, files are placed in the current working directory.

The optional argument `--namespace` is used if the objects are to be placed in a particular namespace or namespace hierarchy (of the format `a::b::c`). If none is given, generated objects are placed in the `dataflow` namespace.


## Next steps

- Automate query generation
    - Based on foreign key relationships, generate member functions that generate queries (or directly return objects) to resolve the dependencies
- Factory classes/methods for making constrained queries à la `SELECT ... FROM ... WHERE ...` in an object-oriented way
- Create objects for views (`CREATE VIEW...`)