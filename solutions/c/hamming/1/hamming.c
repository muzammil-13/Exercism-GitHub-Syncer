#include "hamming.h"
#include <stdio.h>
int compute(const char *l, const char *r) {
  int count = 0;
  if (!l || !r)
    return -1;
  for (; *l != '\0' && *r != '\0'; ++l, ++r) {
    if (*l != *r)
        ++count;
  }
  if (*l != *r)
    return -1;
  return count;
}





