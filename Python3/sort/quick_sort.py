def quick_sort(A):
    if len(A) <= 1:
        return A
    else:
        p = A[0]  # another method: from random import choice and set p = choice(A)
        small_part = [x for x in A[1:] if x < p]
        large_part = [x for x in A[1:] if x >= p]
        return quick_sort(small_part) + [p] + quick_sort(large_part)


def quick_sort_optimize(A):
    less = []
    equal = []
    greater = []

    if len(A) > 1:
        pivot = A[0]
        for x in A:
            if x < pivot:
                less.append(x)
            if x == pivot:
                equal.append(x)
            if x > pivot:
                greater.append(x)
        return quick_sort_optimiz(less) + equal + quick_sort_optimiz(greater)  
    else:  
        return A

