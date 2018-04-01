#include "vector.h"
#include "array.h"

struct _qua_vector {
  qua_array* qa;
  size_t size;
};

qua_vector *qua_vector_create(size_t init_cap) {
  return NULL;
}

size_t qua_vector_size(qua_vector* qv) {
  return 0;
}

void *qua_vector_get(qua_vector* qv, size_t index) {
  return NULL;
}

bool qua_vector_set(qua_vector* qv, size_t index, void *data) {
  return false;
}

bool qua_vector_destroy(qua_vector *qv) {
  return false;
}
