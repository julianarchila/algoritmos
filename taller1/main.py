
from insertion_sort import insertion_sort
from merge_sort import merge_sort

from utils import graph_results, run_test, save_results


algorithms = {
    "insertion_sort": insertion_sort,
    # "merge_sort": merge_sort
    # "tim_sort": 
}


def main() -> None:
    for name, algorithm in algorithms.items():
        print(f"Running test for {name}...")
        res = run_test(algorithm, time=10)
        print(f"Saving results for {name}...")
        save_results(res, f"{name}_results.csv")
        print(f"Graphing results for {name}...")
        graph_results(res, f"{name} Sort")
        print(f"Done with {name}!\n")


if __name__ == "__main__":
    main()

