import random
import time
from typing import List

def generate_random_array(size: int) -> List[int]:
    return [random.randint(1, 5000) for _ in range(size)]


def save_to_json(res: List[dict], filename: str) -> None:
    import json
    with open(filename, "w") as f:
        json.dump(res, f)


def save_to_csv(res: List[dict], filename: str) -> None:
    import pandas as pd
    df = pd.DataFrame(res)
    df.to_csv(filename, index=False)


def save_results(res: List[dict], filename: str, file_format: str = "csv") -> None:
    if file_format == "json":
        save_to_json(res, filename)
    elif file_format == "csv":
        save_to_csv(res, filename)
    else:
        raise ValueError("Invalid file format. Please choose either 'json' or 'csv'.")

# Results looks like this: [{"n": 10, "time": 0.0001}, {"n": 20, "time": 0.0002}, ...]

def graph_results(res: List[dict], title: str, x_label: str = "n", y_label: str = "time") -> None:
    import matplotlib.pyplot as plt
    x = [r["n"] for r in res]
    y = [r["time"] for r in res]
    
    plt.plot(x, y)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.title(title)
    plt.savefig(title + ".png")

    # clean up
    plt.clf()
    plt.cla()




def median(arr: List[float]) -> float:
    n = len(arr)
    sorted_arr = sorted(arr)
    if n % 2 == 0:
        return (sorted_arr[n // 2 - 1] + sorted_arr[n // 2]) / 2
    else:
        return sorted_arr[n // 2]


def run_experiment(n: int, num_experiments: int, algorithm) -> float:
    times = []
    for _ in range(num_experiments):
        arr = generate_random_array(n)
        start_time = time.time()
        algorithm(arr)

        """ if (algorithm.__name__ == "merge_sort"):
            algorithm(arr, 0, len(arr) - 1)
        else:
            algorithm(arr) """

        end_time = time.time()
        times.append(end_time - start_time)
    return median(times)


def run_test(algorithm, time = 300) -> List[dict]:
    n = 1
    total_time = 0
    num_experiments = 100
    res = []
    while total_time < time:
        median_time = run_experiment(n, num_experiments, algorithm=algorithm)
        print(f"For n={n}, median execution time: {median_time:.6f} seconds")
        res.append({"n": n, "time": median_time})
        total_time += median_time * num_experiments
        n += 1

    return res


#inputs should be something like: {"merge_sort": merge_sort_results, "insertion_sort": insertion_sort_results, ...}
#outputs a graph comparing the results of all the algorithms
#lines should be different colors, make sure to include a legend with the names of the algorithms
def graph_results_merged(filePaths: List[str]) -> None:
    #load the results from the files
    import pandas as pd

    names = [file.split("_")[0] for file in filePaths]

    dfs = []
    for file in filePaths:
        dfs.append(pd.read_csv(file))

    #plot the results
    import matplotlib.pyplot as plt
    for df in dfs:
        plt.plot(df["n"], df["time"])
    plt.xlabel("n")
    plt.ylabel("time")
    plt.title("All Results")
    # plt.legend([df.columns[1] for df in dfs])
    plt.legend(names)
    plt.savefig("All Results.png")

    #clean up

    plt.clf()
    plt.cla()

