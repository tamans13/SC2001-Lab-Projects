#include "sorting.h"
#include <algorithm> 

void insertionSortRange(std::vector<int>& slot, int l, int r) {
    for (int i = l + 1; i <= r; i++) {
        for (int j = i; j > l; j--) {
            if (slot[j] < slot[j - 1]) std::swap(slot[j], slot[j - 1]);
            else break;
        }
    }
}

void mergeInPlace(std::vector<int>& slot, int n, int m) {
    if (m - n <= 0) return;
    int mid = (n + m) / 2;

    int a = n;        // left half head
    int b = mid + 1;  // right half head

    while (a <= mid && b <= m) {
        if (slot[a] < slot[b]) {
            a++;
        } else if (slot[a] > slot[b]) {
            int tmp = slot[b++];       // right head
            for (int i = ++mid; i > a; i--) {  // right shift
                slot[i] = slot[i - 1];
            }
            slot[a++] = tmp;           // insert tmp at a
        } else {
            // when slot a equal slot b
            if (a == mid && b == m) break;
            int tmp = slot[b++];
            a++;
            for (int i = ++mid; i > a; i--) {
                slot[i] = slot[i - 1];
            }
            slot[a++] = tmp;
        }
    }
}

void hybridMergeSort(std::vector<int>& slot, int n, int m, int S) {
    int size = m - n + 1;
    if (size <= 1) return;

    // switches to insertion
    if (size <= S) {
        insertionSortRange(slot, n, m);
        return;
    }

    int mid = (n + m) / 2;
    hybridMergeSort(slot, n, mid, S);
    hybridMergeSort(slot, mid + 1, m, S);
    mergeInPlace(slot, n, m);
}