
from insertion_sort import insertion_sort
from merge_sort import merge_sort
from tim_sort import tim_sort

from utils import graph_results_merged, graph_results, run_test, save_results


algorithms = {
    "merge_sort": merge_sort,
    "insertion_sort": insertion_sort,
    "tim_sort": tim_sort,
}


def main() -> None:
    for name, algorithm in algorithms.items():
        res = []
        print(f"Running test for {name}...")
        res = run_test(algorithm, time=300)
        print(f"Saving results for {name}...")
        save_results(res, f"{name}_results.csv")
        print(f"Graphing results for {name}...")
        graph_results(res, f"{name}")
        print(f"Done with {name}!\n")


    print("Graphing all results...")
    graph_results_merged([ f"{name}_results.csv" for name in algorithms.keys()])



if __name__ == "__main__":
    main()

