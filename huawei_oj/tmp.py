s = input()
s = s.strip().split()


def is_str_array(s):
    for i in s:
        if i.isalpha():
            pass
        else:
            return False
    return True


def is_digit_array(s):
    for i in s:
        if i.isdigit():
            pass
        else:
            return False
    return True


def have_one_symbol(s):
    symbol_num = 0
    for i in s:
        if i.isdigit():
            continue
        elif i.isalpha():
            continue
        elif i == '-':
            symbol_num += 1
        else:
            return False
    if symbol_num == 1:
        return True
    else:
        return False


def have_two_symbol(s):
    for i in s:
        if i.isdigit():
            continue
        elif i.isalpha():
            continue
        elif i == '-':
            continue
        else:
            return False
    if '--' in s and s.count('--') == 1:
        tmp = s.split('--')
        if len(tmp) == 2:
            return True
    return False


def have_mix_symbol(s):
    s = s.strip('-')
    if '-' in s:
        return False
    return True


def main():
    singal_str = []
    singal_digit = []
    str_array = []
    digit_array = []
    combine = []
    for item in s:
        item = item.strip()
        if len(item) == 1:
            if item.isalpha():
                singal_str.append(item)
            elif item.isdigit():
                singal_digit.append(item)
        elif is_str_array(item):
            str_array.append(item)
        elif is_digit_array(item):
            digit_array.append(item)
        elif have_one_symbol(item):
            str_array.append(item)
        elif have_two_symbol(item):
            for a in item.split('--'):
                if len(a) == 1:
                    singal_str.append(a)
                else:
                    str_array.append(a)
        elif have_mix_symbol(item):
            str_array.append(item.strip('-'))
        else:
            continue
    res = singal_str + singal_digit + str_array + digit_array + combine
    res = res[::-1]
    print(' '.join(res))


main()
