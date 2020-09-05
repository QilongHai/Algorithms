while True:
    try:
        a, nums, is_sorted_flag = input(), map(int, input().split()), input()
        if is_sorted_flag == '0':
            res = " ".join(map(str, sorted(nums)))
        else:
            res = " ".join(map(str, sorted(nums, reverse=True)))
        print(res)
    except:
        break
