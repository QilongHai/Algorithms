def length_longest_substring(s):
    start = 0
    max_len = 0
    used_char = {}
    for index, value in enumerate(s):
        if value in used_char and start <= used_char[value]:
            start = used_char[value] + 1
        else:
            max_len = max(max_len, index - start + 1)
        used_char[value] = index
    return max_len

if __name__ == '__main__':
    s = 'abcabcbb'
    print(length_longest_substring(s))
    s_ = 'bbbbb'
    print(length_longest_substring(s_))
    s__ = 'pwwkew'
    print(length_longest_substring(s__))