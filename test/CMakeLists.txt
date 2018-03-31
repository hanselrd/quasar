include_directories("${PROJECT_SOURCE_DIR}/includes")

add_executable(test_quasar
  test_main.cpp
  test_array.cpp
)
add_test(test_quasar test_quasar)
target_link_libraries(test_quasar quasar)

if(UNIX)
  add_test(test_quasar_valgrind valgrind
    --error-exitcode=1 --read-var-info=yes
    --leak-check=full --show-leak-kinds=all
    ./test_quasar
  )
endif(UNIX)
