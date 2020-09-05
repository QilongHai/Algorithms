def merge_data_table(d):
    for k in sorted(d.keys()):
        print(k, d[k])


n = int(input())
d = dict()
i = 0
while i < n:
    s = input()
    k, v = s.strip().split()
    k = int(k)
    v = int(v)
    d[k] = d.get(k, 0) + v
    i += 1
merge_data_table(d)