import argparse
import random
import time
from typing import List, Tuple

# run it with python "Lab Project 1/src/part_d/part_d.py" --S 20

def insertion_sort_range(a: List[int], lo: int, hi: int) -> int:
    """Sort a[lo:hi] in-place using insertion sort. Returns key comparison count."""
    comps = 0
    for i in range(lo + 1, hi):
        key = a[i]
        j = i - 1
        while j >= lo:
            comps += 1
            if a[j] > key:
                a[j + 1] = a[j]
                j -= 1
            else:
                break
        a[j + 1] = key
    return comps


def merge_with_aux(a: List[int], aux: List[int], lo: int, mid: int, hi: int) -> int:
    """Merge sorted a[lo:mid] and a[mid:hi] using aux buffer. Returns key comparisons."""
    comps = 0
    aux[lo:hi] = a[lo:hi]
    i = lo
    j = mid
    k = lo
    while i < mid and j < hi:
        comps += 1
        if aux[i] <= aux[j]:
            a[k] = aux[i]
            i += 1
        else:
            a[k] = aux[j]
            j += 1
        k += 1
    while i < mid:
        a[k] = aux[i]
        i += 1
        k += 1
    while j < hi:
        a[k] = aux[j]
        j += 1
        k += 1
    return comps


def merge_sort_original(a: List[int]) -> int:
    """Original mergesort. Returns key comparison count."""
    n = len(a)
    aux = [0] * n

    def sort(lo: int, hi: int) -> int:
        size = hi - lo
        if size <= 1:
            return 0
        mid = lo + size // 2
        comps = sort(lo, mid)
        comps += sort(mid, hi)
        comps += merge_with_aux(a, aux, lo, mid, hi)
        return comps

    return sort(0, n)


def merge_sort_hybrid(a: List[int], S: int) -> int:
    """Hybrid mergesort with insertion sort threshold S. Returns key comparison count."""
    n = len(a)
    aux = [0] * n

    def sort(lo: int, hi: int) -> int:
        size = hi - lo
        if size <= 1:
            return 0
        if size <= S:
            return insertion_sort_range(a, lo, hi)
        mid = lo + size // 2
        comps = sort(lo, mid)
        comps += sort(mid, hi)
        comps += merge_with_aux(a, aux, lo, mid, hi)
        return comps

    return sort(0, n)


def run_once(n: int, x: int, S: int, seed: int) -> None:
    rng = random.Random(seed)
    data = [rng.randint(1, x) for _ in range(n)]

    data_original = list(data)
    data_hybrid = list(data)

    t0 = time.perf_counter()
    comps_original = merge_sort_original(data_original)
    t1 = time.perf_counter()

    t2 = time.perf_counter()
    comps_hybrid = merge_sort_hybrid(data_hybrid, S)
    t3 = time.perf_counter()

    print(f"n = {n} | x = {x} | S = {S} | seed = {seed}")
    print(f"Original mergesort: comps = {comps_original}, time = {t1 - t0:.6f} s")
    print(f"Hybrid mergesort:   comps = {comps_hybrid}, time = {t3 - t2:.6f} s")


def main() -> None:
    parser = argparse.ArgumentParser(description="Part D: compare original mergesort vs hybrid mergesort")
    parser.add_argument("--n", type=int, default=10_000_000, help="input size")
    parser.add_argument("--x", type=int, default=10_000_000, help="max integer value")
    parser.add_argument("--S", type=int, default=20, help="hybrid insertion threshold")
    parser.add_argument("--seed", type=int, default=12345, help="random seed")
    args = parser.parse_args()

    run_once(args.n, args.x, args.S, args.seed)


if __name__ == "__main__":
    main()