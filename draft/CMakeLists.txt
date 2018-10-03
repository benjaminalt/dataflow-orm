cmake_minimum_required(VERSION 2.8.9)
project (test)
# find_package(Boost REQUIRED)
include_directories(
    include
    # ${Boost_INCLUDE_DIRS}
)
add_executable(test main.cpp)