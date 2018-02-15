def merge_sort(A):
    if len(A) < 2:
        return A
    else:
        mid = len(A) // 2
        left_part = A[:mid]
        right_part = A[mid:]
        merge_sort(left_part)
        merge_sort(right_part)

        i = 0
        j = 0
        k = 0
        while i < len(left_part) and j < len(right_part):
            if left_part[i] < right_part[j]:
                A[k] = left_part[i]
                i += 1
            else:
                A[k] = right_part[j]
                j += 1
            k += 1
        while i < len(left_part):
            A[k] = left_part[i]
            i += 1
            k += 1
        while j < len(right_part):
            A[k] = right_part[j]
            j += 1
            k += 1
