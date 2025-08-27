#include "leap.h"

bool leap_year(int year) {
    return year % 4 == 0 && (year % 100 != 0 || year % 400 == 0);
}





#ifndef LEAP_H
#define LEAP_H

#include <stdbool.h>

bool leap_year(int year);

#endif