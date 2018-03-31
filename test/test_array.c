#include <stdio.h>
#include "array.h"

int main(int argc, char** argv) {
  printf("not null %d\n", qua_array_create(1) != NULL);
  return 0;
}
