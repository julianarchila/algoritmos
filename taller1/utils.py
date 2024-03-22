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
        end_time = time.time()
        times.append(end_time - start_time)
    return median(times)
