#ifndef QUA_ARRAY_H
#define QUA_ARRAY_H

#include <stdbool.h>
#include <stddef.h>

typedef void qua_array;

qua_array *qua_array_create(size_t size);

size_t qua_array_size(qua_array* qa);

void *qua_array_get(qua_array* qa, size_t index);

bool qua_array_set(qua_array* qa, size_t index, void *data);

bool qua_array_destroy(qua_array *qa);

#endif
