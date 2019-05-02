def reverse_integer(x):
    if x < 0:
        x = int(str(x)[::-1][-1] + str(x)[::-1][:-1])
    else:
        x = int(str(x)[::-1])
    x = 0 if abs(x) > 0x7FFFFFFF else x
    return x


if __name__ == '__main__':
    x = -123
    print(reverse_integer(x))
    print('')
    y = 123
    print(reverse_integer(y))