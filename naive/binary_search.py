def f_recursion(data, target, low, high):
    if low > high:
        return False
    else:
        mid = (low + high) // 2
        if target == data[mid]:
            return mid
        elif target < data[mid]:
            return f_recursion(data, target, low, mid-1)
        else:
            return f_recursion(data, target, mid+1, high)

def f_iterative(data, target):
    low = 0
    high = len(data) - 1
    while low <= high:
        mid = (low + high) // 2
        if target == data[mid]:
            return mid
        elif target < data[mid]:
            high = mid - 1
        else:
            low = mid + 1
    return False

if __name__ == '__main__':
    data = [n for n in range(101)]
    print(data)
    target = 23
    print(f_recursion(data, target, 0, 100))
    print(f_iterative(data, target))