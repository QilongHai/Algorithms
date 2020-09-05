def compute_str_num(s):
    tmp = set()
    for i in s:
        if 0 <= ord(i) <= 127:
            tmp.add(i)
    return len(tmp)

s = input()
print(compute_str_num(s))