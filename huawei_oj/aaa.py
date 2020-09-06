def is_num(s):
    try:
        float(s)
    except:
        return False
    if '.' in s:
        idx = s.index('.')
        try:
            if s[idx-1].isdigit() and s[idx+1].isdigit():
                return True
        except:
            return False
    return True

def main():
    s = input()
    s = s.strip()
    sub = []
    max_len = 0
    for i in range(len(s)-1):
        for j in range(i+1, len(s)):
            tmp = s[i:j]
            if is_num(tmp):
                if len(tmp) > max_len:
                    max_len = len(tmp)
                sub.append(tmp)
    d = dict()
    for i in sub:
        if len(i) == max_len:
            if max_len not in d:
                d[max_len] = [i]
            else:
                d[max_len].append(i)
    if max_len == 0:
        print('')
    else:
        print(d[max_len][-1])

main()
