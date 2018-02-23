def kmp(target_str, pattern_str, p_next):
    i, j = 0, 0
    m = len(pattern_str)
    n = len(target_str)
    while i < m and j < n:
        if i == -1 or target_str[j] == pattern_str[i]:
            i += 1
            j += 1
        else:
            i = p_next[i]
    if i == m:
        return j - i
    return -1

def gen_pnext(p):
    i = 0
    k = -1
    m = len(p)
    p_next = m * [-1]
    while i < m - 1:
        if k == -1 or p[i] == p[k]:
            i += 1
            k += 1
            p_next[i] = k
        else:
            k = p_next[k]
    return p_next
