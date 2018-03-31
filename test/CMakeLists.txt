include_directories("${PROJECT_SOURCE_DIR}/includes")

add_executable(test_array test_array.c)
add_test(test1 test_array)
target_link_libraries(test_array quasar)
