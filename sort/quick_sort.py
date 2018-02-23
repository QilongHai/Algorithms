def quick_sort(A):
    if len(A) <= 1:
        return A
    else:
        p = A[0]  # another method: from random import choice and set p = choice(A)
        small_part = [x for x in A[1:] if x < p]
        large_part = [x for x in A[1:] if x >= p]
        return small_part + [p] + large_part

