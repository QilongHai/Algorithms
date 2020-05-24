from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        if not nums:
            return []
        n = len(nums)
        L = [1 for _ in range(n)]
        R = [1 for _ in range(n)]
        L[0] = 1
        for i in range(1, n):
            L[i] = L[i - 1] * nums[i - 1]
        R[-1] = 1
        for j in range(n - 1)[::-1]:
            R[j] = R[j + 1] * nums[j + 1]
        res = [L[k] * R[k] for k in range(n)]
        return res

# 算法：
# 1. 初始化两个空数组 L 和 R。对于给定索引 i，L[i] 代表的是 i 左侧所有数字的乘积，R[i] 代表的是 i 右侧所有数字的乘积。
# 2. 我们需要用两个循环来填充 L 和 R 数组的值。对于数组 L，L[0] 应该是 1，因为第一个元素的左边没有元素。
# 对于其他元素：L[i] = L[i-1] * nums[i-1]。
# 3. 同理，对于数组 R，R[length-1] 应为 1。length 指的是输入数组的大小。其他元素：R[i] = R[i+1] * nums[i+1]。
# 4. 当 R 和 L 数组填充完成，我们只需要在输入数组上迭代，且索引 i 处的值为：L[i]*R[i]
