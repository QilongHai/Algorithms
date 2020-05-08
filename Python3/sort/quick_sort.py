def quick_sort_recursion(A):
    if len(A) <= 1:
        return A
    else:
        p = A[0]  # another method: from random import choice and set p = choice(A)
        small_part = [x for x in A[1:] if x < p]
        large_part = [x for x in A[1:] if x >= p]
        return quick_sort_recursion(small_part) + [p] + quick_sort_recursion(large_part)


def quick_sort_clear(A):
    less = []
    equal = []
    greater = []

    if len(A) > 1:
        pivot = A[0]
        for x in A[1:]:
            if x < pivot:
                less.append(x)
            if x == pivot:
                equal.append(x)
            if x > pivot:
                greater.append(x)
        return quick_sort_clear(less) + equal + quick_sort_clear(greater)
    else:
        return A


def quick_sort(A):
    return qsort(A, 0, len(A) - 1)

def qsort(A, left, right):
    if left >= right : return A
    key = A[left]     #取最左边的为基准数
    i = left           #左指针
    j = right          #右指针
    while i < j :
        while A[j] >= key and i < j :
            j -= 1
        while A[i] <= key and i < j :
            i += 1
        A[i], A[j] = A[j], A[i]
    A[left], A[i] = A[i], A[left]
    qsort(A, left, i - 1)
    qsort(A, j + 1, right)
    return A