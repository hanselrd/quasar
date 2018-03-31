#include "Catch2/single_include/catch.hpp"
extern "C" {
  #include "array.h"
}

TEST_CASE("[array]") {
  SECTION("created with a size of 0 should return NULL") {
    qua_array *qa = qua_array_create(0);
    REQUIRE(qa == NULL);
    qua_array_destroy(qa);
  }

  SECTION("created with a size greater than 0 should NOT return NULL") {
    qua_array *qa = qua_array_create(1);
    REQUIRE(qa != NULL);
    qua_array_destroy(qa);
  }
}
