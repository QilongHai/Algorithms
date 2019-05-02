def f1(n):
    if n < 2: 
        return 1
    else: 
        return f1(n-1) + f1(n-2)


def f2(n):
    if n < 2: 
        return 1
    memo = [1, 1]
    for i in range(2, n+1):
        memo.append(memo[i-1] + memo[i-2])
    return memo[n]


def f3(n):
    memo = {}
    if n in memo:
        return memo[n]
    else:
        if n < 2:
            f = 1
        else:
            f = f3(n-1) + f3(n-2)
        memo[n] = f
        return f


if __name__ == '__main__':
    n = 23
    print(f1(n))
    print(f2(n))
    print(f3(n))