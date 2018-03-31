#include "array.h"
#include <stdlib.h>

struct _qua_array {
  size_t size;
  void **data;
};

qua_array *qua_array_create(size_t size) {
  if (size > 0) {
    qua_array *qa = malloc(sizeof(qua_array));
    if (qa != NULL) {
      qa->data = malloc(sizeof(size) * sizeof(void *));
      if (qa->data != NULL) {
        qa->size = size;
        return qa;
      }
      free(qa);
    }
  }
  return NULL;
}

size_t qua_array_size(qua_array* qa) {return 0;}

void *qua_array_get(qua_array* qa, size_t index) {return NULL;}

bool qua_array_set(qua_array* qa, size_t index, void *data) {return false;}

void qua_array_destroy(qua_array *qa) {
  if (qa != NULL) {
    if (qa->data != NULL) {
      free(qa->data);
    }
    free(qa);
  }
}
