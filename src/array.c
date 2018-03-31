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

void qua_array_destroy(qua_array *qa) {
  if (qa != NULL) {
    if (qa->data != NULL) {
      free(qa->data);
    }
    free(qa);
  }
}
