from typing import List


# class Solution:
#     def permute(self, nums: List[int]) -> List[List[int]]:
#         res = []
#
#         def helper(nums, tmp):
#             if not nums:
#                 res.append(tmp)
#                 return
#             for i in range(len(nums)):
#                 print(tmp+[nums[i]])
#                 helper(nums[:i] + nums[i + 1:], tmp + [nums[i]])
#
#         helper(nums, [])
#         return res


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        def dfs(nums, size, depth, hash_set, path, res):
            if depth == size:
                res.append(path[:])
                return
            for i in range(size):
                if nums[i] not in hash_set:
                    hash_set.add(nums[i])
                    path.append(nums[i])
                    dfs(nums, size, depth+1, hash_set, path, res)
                    path.pop()
                    hash_set.remove(nums[i])

        size = len(nums)
        if size == 0:
            return []
        path = []
        res = []
        hash_set = set()
        dfs(nums, size, 0, hash_set, path, res)
        return res


s = Solution()
nums = [1, 2, 3]
print(nums[:])

