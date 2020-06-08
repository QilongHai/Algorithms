from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        max_len = 0
        num_set = set(nums)
        for num in num_set:
            if num - 1 in num_set:
                continue
            else:
                cur_num = num
                cur_len = 1
                while cur_num + 1 in num_set:
                    cur_num += 1
                    cur_len += 1
                max_len = max(max_len, cur_len)
        return max_len



class SolutionTwo:
    def longestConsecutive(self, nums: List[int]) -> int:
        d = dict()
        max_len = 0
        for num in nums:
            left = d.get(num - 1, 0)
            right = d.get(num + 1, 0)
            cur_len = 1 + left + right
            max_len = max(max_len, cur_len)

            d[num] = cur_len
            d[num - left] = cur_len
            d[num + right] = cur_len
        return max_len
        


