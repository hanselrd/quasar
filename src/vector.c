#include "vector.h"
#include "array.h"

typedef struct {
  qua_array* qa;
  size_t size;
} qua_vector;

qua_vector *qua_vector_create(size_t init_cap) {
  return NULL;
}

int qua_vector_size(qua_vector* qv) {
  return -1;
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
