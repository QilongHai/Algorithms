def heap_sort(data):
    def sift_down(data, e, start, end):
        i, j = start, start * 2 + 1
        while j < end:
            if j+1 < end and data[j+1] < data[j]:
                j += 1
            if e < data[j]:
                break
            data[i] = data[j]
            i, j = j, 2 * j + 1
        data[i] = e

    end = len(data)
    for i in range(end // 2, -1, -1):
        sift_down(data, data[i], i, end)
    for i in range(end-1, 0, -1):
        e = data[i]
        data[i] = data[0]
        sift_down(data, e, 0, i)
