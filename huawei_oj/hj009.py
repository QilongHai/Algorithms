def generate_new_num(num):
    stack = []
    while num:
        digit = num % 10
        if digit not in stack:
            stack.append(digit)
        else:
            pass
        num //= 10
    res = 0
    for i in stack:
        res = res * 10 + i
    return res

num = int(input())
res = generate_new_num(num)
print(res)