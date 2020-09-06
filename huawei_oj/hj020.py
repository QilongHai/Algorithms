import sys


def is_len_valid(s):
    if len(s) <= 8:
        return False
    return True


def is_substr_valid(s):
    sub_str_list = []
    for i in range(len(s) - 2):
        sub_str_list.append(s[i:i + 3])
    if len(set(sub_str_list)) != len(sub_str_list):
        return False
    return True


def is_classfiy_valid(s):
    up_flag = 0
    low_flag = 0
    digit_flag = 0
    symbol_flag = 0
    for i in s:
        if i.isupper():
            up_flag = 1
        elif i.islower():
            low_flag = 1
        elif i.isdigit():
            digit_flag = 1
        else:
            symbol_flag = 1
    if up_flag + low_flag + digit_flag + symbol_flag >= 3:
        return True
    return False


def main(line):
    len_flag = is_len_valid(line)
    sub_flag = is_substr_valid(line)
    classfiy_flag = is_classfiy_valid(line)
    if len_flag and sub_flag and classfiy_flag:
        print('OK')
    else:
        print('NG')

main(input())
