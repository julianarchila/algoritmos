from typing import List

from utils import run_experiment, save_results  


def insertion_sort(arr: List[int]) -> None:
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key


def main() -> None:
    n = 1
    total_time = 0
    num_experiments = 100
    res = []
    while total_time < 10:
        median_time = run_experiment(n, num_experiments, algorithm=insertion_sort)
        print(f"For n={n}, median execution time: {median_time:.6f} seconds")
        res.append({"n": n, "time": median_time})
        total_time += median_time * num_experiments
        n += 1


    save_results(res, "insertion_sort_results.csv")

if __name__ == "__main__":
    main()

