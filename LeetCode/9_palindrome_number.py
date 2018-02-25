def palindrome_number(x):
    if x < 0:
        return False
    copy, reverse = x, 0

    while copy:
        reverse *= 10
        reverse += copy % 10
        copy //= 10

    return x == reverse

if __name__ == '__main__':
    print(palindrome_number(12321))
    print(palindrome_number(12344321))
    print(palindrome_number(1223343221))