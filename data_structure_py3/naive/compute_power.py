def power_fast(x, n):
    if n == 0:
        return 1
    else:
        partial = power_fast(x, n // 2)
        result = partial * partial
        if n % 2 == 1:
            result = result * x
        return result

def power_slow(x, n):
    if n == 0:
        return 1
    else:
        return x * power_slow(x, n-1)

if __name__ == '__main__':
    x = 2
    n = 22
    print(power_fast(x, n))
    print(power_slow(x, n))