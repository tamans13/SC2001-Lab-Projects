#ifndef GENERATOR_H
#define GENERATOR_H

#include <vector>
#include <random>

std::vector<int> generateRandomArray(int n, int x, std::mt19937& rng);
std::vector<int> makeSizeSchedule();

#endif