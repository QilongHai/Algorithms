def f(target_str, pattern_str):
    m = len(pattern_str)
    n = len(target_str)
    i = 0
    j = 0
    while i < m and j < n:
        if pattern_str[i] == target_str[j]:
            i += 1
            j += 1
        else:
            i = 0
            j = j - i + 1
    if i == m:
        return j - i  # find a pattern string, and return the index of start
    return None

if __name__ == '__main__':
    t = 'abcdabcdabcacd'
    p = 'acd'
    print(f(t, p))