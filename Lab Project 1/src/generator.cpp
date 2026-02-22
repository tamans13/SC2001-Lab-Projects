#include "generator.h"

std::vector<int> generateRandomArray(int n, int x, std::mt19937& rng) {
    std::uniform_int_distribution<int> dist(1, x);
    std::vector<int> a(n);
    for (int i = 0; i < n; i++)
        a[i] = dist(rng);
    return a;
}

std::vector<int> makeSizeSchedule() {
    return {
        1000, 2000, 5000,
        10000, 20000, 50000,
        100000, 200000, 500000,
        1000000, 2000000, 5000000,
        10000000
    };
}