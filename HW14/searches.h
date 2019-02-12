// searches.h

#ifndef _SEARCHES_H
#define _SEARCHES_H


int linear_search(const int *a, int size, int m);
// a is an array, size is the size of the array and m is the integer to find
// post: returns the idex of the item in the array, or -1 if the item is not present

int binary_search(const int *a, int size, int m);
// a is an array, size is the size of the array and m is the integer to find
// pre: elements of a must be sorted in increasing order
// post: returns the idex of the item in the array, or -1 if the item is not present

#endif
