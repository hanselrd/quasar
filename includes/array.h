#ifndef QUA_ARRAY_H
#define QUA_ARRAY_H

#include <stddef.h>

typedef struct _qua_array qua_array;

qua_array* qua_array_create(size_t size);
void qua_array_destroy(qua_array* qa);

#endif
