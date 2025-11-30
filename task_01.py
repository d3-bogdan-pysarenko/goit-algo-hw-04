import random
import timeit
from statistics import mean


# -------------------------------------------------------------------------------------
def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return merge(left, right)


def merge(left, right):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])
    return result

# -------------------------------------------------------------------------------------

def insertion_sort(arr):
    arr = arr[:]  # make copy
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1

        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = key
    return arr


# -------------------------------------------------------------------------------------

def timsort(arr):
    return sorted(arr)


# -------------------------------------------------------------------------------------
#                                  MEASUREMENT HELPERS
# -------------------------------------------------------------------------------------
def time_callable(callable_fn, repeats=3, number=3):
    """
    Виконує timeit для callable_fn:
      - repeats: кількість окремих викликів timeit (збираємо середнє)
      - number: скільки разів виконується callable у одному timeit
    Повертає середній час одного виконання (time per single call).
    """
    t = timeit.Timer(callable_fn)
    times = [t.timeit(number=number) / number for _ in range(repeats)]
    return mean(times)


# -----------------------------
#      BENCHMARK
# -----------------------------
def benchmark():
    sizes = [10, 100, 500, 1000, 2000, 5000, 10000]  # sets initializing
    repeats = 3
    number = 3

    for n in sizes:
        print(f"\n=== n = {n} ===")

        # creating Random, already sorted and sorted-reversed
        base_random = [random.randint(0, 1000000) for _ in range(n)]
        base_sorted = sorted(base_random)
        base_reversed = list(reversed(base_sorted))

        datasets = [
            ("random", base_random),
            ("sorted", base_sorted),
            ("reversed", base_reversed),
        ]

        for dtype, base in datasets:
            print(f"\n-- dataset: {dtype} --")

            # wrapper, for array copy
            def run_merge():
                # using copy instead of original array
                merge_sort(base[:])

            def run_insertion():
                insertion_sort(base[:])

            def run_timsort():
                timsort(base[:])

            # Limiting Insertion to 5k since it takes too long on bigger data
            if n > 5000:
                insert_time = None
                print("Insertion sort: skipped (n too large)")
            else:
                insert_time = time_callable(run_insertion, repeats=repeats, number=number)
                print(f"Insertion sort: {insert_time:.6f} s (avg per run)")

            merge_time = time_callable(run_merge, repeats=repeats, number=number)
            tim_time = time_callable(run_timsort, repeats=repeats, number=number)

            print(f"Merge sort:     {merge_time:.6f} s (avg per run)")
            print(f"Timsort:        {tim_time:.6f} s (avg per run)")


if __name__ == "__main__":
    benchmark()
