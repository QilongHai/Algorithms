s = input()
from collections import OrderedDict

d = OrderedDict()
for i in s:
    d[i] = d.get(i, 0) + 1
min_times = min(list(d.values()))
tmp = []
for k, v in d.items():
    if v == min_times:
        tmp.append(k)
res = []
for i in s:
    if i not in tmp:
        res.append(i)
print(''.join(res))
