def bubble_sort(data):
    for i in range(len(data)):
        for j in range(1, len(data)-i):
            if data[j-1] > data[j]:
                data[j-1], data[j] = data[j], data[j-1]

def bubble_sort_opt(data):
    for i in range(len(data)):
        found = False
        for j in range(1, len(data)-i):
            if data[j-1] > data[j]:
                data[j-1], data[j] = data[j], data[j-1]
                found = True
        if not found:
            break