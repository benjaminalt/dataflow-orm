from unittest import TestCase
from ddt import ddt, data, unpack
import os
import shutil
from subprocess import call

from generator.generate import generate

SCRIPT_DIR = os.path.dirname(os.path.realpath(__file__))
SCHEMA_DIR = os.path.join(SCRIPT_DIR, os.pardir, "schemas")
OUTPUT_DIR = os.path.join(SCRIPT_DIR, os.pardir, "output")


def clear_directory(dirpath):
    if os.path.exists(dirpath):
        for item in os.listdir(dirpath):
            item_path = os.path.join(dirpath, item)
            if os.path.isfile(item_path):
                os.unlink(item_path)
            else:
                shutil.rmtree(item_path)


@ddt
class TestGenerate(TestCase):
    def setUp(self):
        if os.path.exists(OUTPUT_DIR):
            clear_directory(OUTPUT_DIR)
        else:
            os.makedirs(OUTPUT_DIR)

    @data(*os.listdir(SCHEMA_DIR))
    def test_generate(self, schema):
        oldcwd = os.getcwd()

        clear_directory(OUTPUT_DIR)
        schema_filepath = os.path.join(SCHEMA_DIR, schema)
        generate("test", schema_filepath, OUTPUT_DIR, "a::b::c")

        # Build
        build_dir = os.path.join(OUTPUT_DIR, "build")
        os.makedirs(build_dir)
        os.chdir(build_dir)
        res = call(["cmake", ".."])
        self.assertEqual(res, 0)
        res = call(["cmake", "--build", "."])
        self.assertEqual(res, 0)

        os.chdir(oldcwd)
