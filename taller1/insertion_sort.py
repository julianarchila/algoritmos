from typing import List

def insertion_sort(arr: List[int]) -> None:
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key


def insertion_sort_with_range(arr: List[int], p: int, r: int) -> None:
    for i in range(p + 1, r + 1):
        key = arr[i]
        j = i - 1
        while j >= p and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
