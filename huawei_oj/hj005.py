def convert_num(s):
    d = {'A': 10, 'B': 11, 'C': 12,
         'D': 13, 'E': 14, 'F': 15}
    for i in range(10):
        d[str(i)] = i
    res = 0
    s = s[2:]
    for i in s[::-1]:
        res = res * 16 + d[i]
    return res


s = input()
print(convert_num(s))
