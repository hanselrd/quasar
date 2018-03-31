find_package(PythonInterp)

if(PYTHON_EXECUTABLE)
  add_test(
    NAME test_quasar
    COMMAND ${PYTHON_EXECUTABLE} -m unittest discover -v
    WORKING_DIRECTORY ${PROJECT_SOURCE_DIR}
  )
endif(PYTHON_EXECUTABLE)
