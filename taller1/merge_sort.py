from typing import List


def merge(a: List[int], p:int, q:int, r:int) -> List[int]:
    nl = q -p + 1
    nr = r -1

    L : List[int] = []
    R : List[int] = []



    for i in range(0, nl):
        L.append(a[p+i])


    for i in range(0, nr):
        R.append(a[q+i+1])


    i = 0
    j = 0
    k = p


    while (i < nl and j < nr):
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


def merge_sort(a: List[int], p:int, r:int) -> List[int]:
    if p < r:
        q = (p + r) // 2
        merge_sort(a, p, q)
        merge_sort(a, q+1, r)
        merge(a, p, q, r)
    return a

