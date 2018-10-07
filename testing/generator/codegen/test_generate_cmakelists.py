from unittest import TestCase
from generator.codegen.generate_cmake import generate_cmakelists


class TestGenerateCmakelists(TestCase):
    def test_generate_cmakelists(self):
        expected = """cmake_minimum_required(VERSION 2.8.9)
project(test)
find_package(Boost REQUIRED)

include_directories(
    include
    ${Boost_INCLUDE_DIRS}
)
add_executable(test main.cpp)
"""
        res = generate_cmakelists("test")
        self.assertEqual(expected, res)
