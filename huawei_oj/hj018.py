import sys


def is_valid(ip_str, mask):
    if not ip_str:
        return False
    if '*' in ip_str:
        return False
    try:
        ip_list = [int(i) for i in ip_str.split('.')]
    except:
        return False
    if len(ip_list) < 4:
        return False
    mask_list = [int(i) for i in mask.split('.')]
    mask_bin_str = ''.join(['{:08b}'.format(i) for i in mask_list])
    zero_flag = mask_bin_str.find('0')
    one_flag = mask_bin_str.find('1')
    if zero_flag == -1 or one_flag == -1 or zero_flag != one_flag + 1:
        return False
    return True


def classify_ip(ip_str):
    ip_list = [int(i) for i in ip_str.strip().split('.')]
    if 1 <= ip_list[0] <= 126:
        return 'a'
    elif 128 <= ip_list[0] <= 191:
        return 'b'
    elif 192 <= ip_list[0] <= 223:
        return 'c'
    elif 224 <= ip_list[0] <= 239:
        return 'd'
    elif 240 <= ip_list[0] <= 255:
        return 'e'
    else:
        return 'err'


def is_private_ip(ip_str):
    ip_list = [int(i) for i in ip_str.strip().split('.')]
    if (ip_list[0] == 10) or \
            (ip_list[0] == 172 and (16 <= ip_list[1] <= 31)) or \
            (ip_list[0] == 192 and ip_list[1] == 168):
        return True
    return False


def main():
    d = dict()
    for line in sys.stdin:
        ip_str, mask = line.strip().split('~')
        if is_valid(ip_str, mask):
            ip_tag = classify_ip(ip_str)
            d[ip_tag] = d.get(ip_tag, 0) + 1
            if is_private_ip(ip_str):
                d['private'] = d.get('private', 0) + 1
        else:
            d['err'] = d.get('err', 0) + 1
    res = []
    for i in ['a', 'b', 'c', 'd', 'e', 'err', 'private']:
        res.append(str(d.get(i, 0)))
    print(' '.join(res))


main()
