#include "Catch2/single_include/catch.hpp"
extern "C" {
  #include "array.h"
}

class qua_array_fixture {
  public:
    qua_array_fixture() : qa(NULL) {}
    ~qua_array_fixture() {
      if (qa != NULL) {
        qua_array_destroy(qa);
      }
    }
  protected:
    qua_array *qa;
};

TEST_CASE_METHOD(qua_array_fixture, "qua_array_create returns NULL on size of 0", "[qua_array]") {
  qa = qua_array_create(0);
  REQUIRE(qa == NULL);
}

TEST_CASE_METHOD(qua_array_fixture, "qua_array_create returns non-NULL on size > 0", "[qua_array]") {
  qa = qua_array_create(1);
  REQUIRE(qa != NULL);
}

TEST_CASE_METHOD(qua_array_fixture, "qua_array_size returns 0 on qa == NULL", "[qua_array]") {
  REQUIRE(qua_array_size(qa) == 0);
}

TEST_CASE_METHOD(qua_array_fixture, "qua_array_size returns non-zero on qa != NULL", "[qua_array]") {
  qa = qua_array_create(2);
  REQUIRE(qua_array_size(qa) == 2);
}
