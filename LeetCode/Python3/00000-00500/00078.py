from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def helper(start, path):
            res.append(path[:])
            for i in range(start, n):
                path.append(nums[i])
                helper(i + 1, path)
                path.pop()

        res = []
        n = len(nums)
        helper(0, [])
        return res


class SolutionTwo:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        for i in range(2 ** len(nums)):
            sub = []
            for j in range(len(nums)):
                if i >> j & 1:
                    sub.append(nums[j])
            res.append(sub)
        return res

    """
    1<<nums.length 等价于 2^nums.length,对于n个数字的数组，共2^n个子集；
    以0~(2^n)-1，2^n个n位二进制数，对应于所有子集，从后往前第 j 个二进制位为 0 表示不放入第 j 个元素,同理1表示放入。" 
    ((i >> j) & 1) == 1 " 表示对于二进制数i，从低位到高位逐个取其二进制位，并判断是否为1，若为1则放入对于nums中的元素。
    """
