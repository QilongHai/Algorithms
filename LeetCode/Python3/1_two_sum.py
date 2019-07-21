def two_sum_naive(nums, target):
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]

def two_sum_hash(nums, target):
    d = dict()
    for index, value in enumerate(nums):
        tmp = target - value
        if tmp in d:
            return [index, d[tmp]]
        else:
            d[value] = index


if __name__ == '__main__':
    nums = [1, 2, 4, 5, 9, 13]
    target = 14
    print(two_sum_hash(nums, target))

    nums_ = [1, 1]
    target_ = 2
    print(two_sum_hash(nums_, target_))