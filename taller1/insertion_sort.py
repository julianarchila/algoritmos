import random
import time
from typing import List

def insertion_sort(arr: List[int]) -> None:
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

def generate_random_array(size: int) -> List[int]:
    return [random.randint(1, 5000) for _ in range(size)]

def median(arr: List[float]) -> float:
    n = len(arr)
    sorted_arr = sorted(arr)
    if n % 2 == 0:
        return (sorted_arr[n // 2 - 1] + sorted_arr[n // 2]) / 2
    else:
        return sorted_arr[n // 2]

def run_experiment(n: int, num_experiments: int) -> float:
    times = []
    for _ in range(num_experiments):
        arr = generate_random_array(n)
        start_time = time.time()
        insertion_sort(arr)
        end_time = time.time()
        times.append(end_time - start_time)
    return median(times)

def main() -> None:
    n = 1
    total_time = 0
    num_experiments = 100
    while total_time < 300:
        median_time = run_experiment(n, num_experiments)
        print(f"For n={n}, median execution time: {median_time:.6f} seconds")
        total_time += median_time * num_experiments
        n += 1

if __name__ == "__main__":
    main()

