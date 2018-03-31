include_directories("${PROJECT_SOURCE_DIR}/includes")
set(src array.c)
add_library(quasar SHARED ${src})
add_library(quasar-s STATIC ${src})
