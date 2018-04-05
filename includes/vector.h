#ifndef QUA_VECTOR_H
#define QUA_VECTOR_H

#include <stdbool.h>
#include <stddef.h>

typedef void qua_vector;

qua_vector *qua_vector_create(size_t init_cap);

int qua_vector_size(qua_vector* qv);

void *qua_vector_get(qua_vector* qv, size_t index);

bool qua_vector_set(qua_vector* qv, size_t index, void *data);

bool qua_vector_destroy(qua_vector *qv);

#endif
