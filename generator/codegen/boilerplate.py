from .. import config

header_comment = """/**
* dataflow version {}
**/
""".format(config.version)

pragma = "#pragma once\n"
