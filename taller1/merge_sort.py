from typing import List

def merge(a: List[int], p:int, q:int, r:int) -> List[int]:
    nl = q - p + 1
    nr = r - q

    L = [0] * nl
    R = [0] * nr

    for i in range(nl):
        L[i] = a[p+i]

    for j in range(nr):
        R[j] = a[q+j+1]

    i = 0
    j = 0
    k = p

    while i < nl and j < nr:
        if L[i] <= R[j]:
            a[k] = L[i]
            i += 1
        else:
            a[k] = R[j]
            j += 1
        k += 1

    while i < nl:
        a[k] = L[i]
        i += 1
        k += 1

    while j < nr:
        a[k] = R[j]
        j += 1
        k += 1

    return a

def _merge_sort(a: List[int], p:int, r:int) -> List[int]:
    if p < r:
        q = (p + r) // 2
        _merge_sort(a, p, q)
        _merge_sort(a, q+1, r)
        merge(a, p, q, r)
    return a

def merge_sort(a: List[int]):
    return _merge_sort(a, 0, len(a)-1)

""" # Example usage:
arr = [12, 11, 13, 5, 6, 7]
n = len(arr)
print("Given array is", arr)
merge_sort(arr, 0, n-1)
print("Sorted array is", arr) """

