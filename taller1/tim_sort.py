from typing import List
# Function to perform Tim Sort
from insertion_sort import insertion_sort_with_range
from merge_sort import merge


def tim_sort(arr: List[int]) -> List[int]:
    n = len(arr)
    min_run = 32

    # Perform insertion sort for each run whose length is less than min_run
    for i in range(0, n, min_run):
        insertion_sort_with_range(arr, i, min((i + min_run - 1), (n - 1)))

    # Start merging from size min_run. Size is doubled on each iteration
    size = min_run
    while size < n:
        for left in range(0, n, 2 * size):
            mid = left + size - 1
            right = min((left + 2 * size - 1), (n - 1))

            if mid < right:
                merge(arr, left, mid, right)
        size *= 2

    return arr

