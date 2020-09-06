import sys
s = input()
x = 0
y = 0

for item in s.split(';'):
    if len(item) == 3:
        if item[0] in ['A', 'D', 'S', 'W'] and item[1].isdigit() and item[2].isdigit():
            d = item[:1]
            step = int(item[1:])
            if d == 'A':
                x -= step
            elif d == 'D':
                x += step
            elif d == 'W':
                y += step
            elif d == 'S':
                y -= step
    elif len(item) == 2:
        if item[0] in ['A', 'D', 'S', 'W'] and item[1].isdigit():
            d = item[0]
            step = int(item[1])
            if d == 'A':
                x -= step
            elif d == 'D':
                x += step
            elif d == 'W':
                y += step
            elif d == 'S':
                y -= step
            d.isd

print(str(x)+','+str(y))
