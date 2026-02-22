#include <iostream>
#include <chrono>
#include "sorting.h"
#include "generator.h"

int main() {
    std::mt19937 rng(std::random_device{}());
    int x = 10000000;   // max value
    int S = 20;         // threshold, change ltr dur testing

    std::vector<int> sizes = makeSizeSchedule();

    for (int n : sizes) {

        std::vector<int> arr = generateRandomArray(n, x, rng);

        auto start = std::chrono::high_resolution_clock::now();

        hybridMergeSort(arr, 0, n - 1, S);

        auto end = std::chrono::high_resolution_clock::now();

        std::chrono::duration<double> elapsed = end - start;

        std::cout << "n = " << n
                  << " | time = " << elapsed.count()
                  << " seconds\n";
    }

    return 0;
}