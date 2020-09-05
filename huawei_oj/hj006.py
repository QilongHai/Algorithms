def solve_prime(num):
    res = []
    for i in range(2, num+1):
        if num % i == 0:
            res.append(i)
            num //= i
    return res

num = int(input())
res = solve_prime(num)
res.append('')
print(res)