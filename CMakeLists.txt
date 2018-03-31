cmake_minimum_required(VERSION 3.2)

project(quasar)

set(CMAKE_BUILD_TYPE Debug)

include_directories(includes)

file(GLOB SOURCES "src/**/*.c")

add_library(quasar ${SOURCES})

# add_executable(tests ${TESTS})
# target_link_libraries(tests ris_c)
