#ifndef SORTING_H
#define SORTING_H

#include <vector>

void insertionSortRange(std::vector<int>& slot, int l, int r);
void mergeInPlace(std::vector<int>& slot, int n, int m);
void hybridMergeSort(std::vector<int>& slot, int n, int m, int S);

#endif