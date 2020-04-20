class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        def helper(nums, tmp_list):
            if not nums:
                res.append(tmp_list)
                return
            for i in range(len(nums)):
                if i > 0 and nums[i] == nums[i-1]:
                    continue
                helper(nums[:i]+nums[i+1:], tmp_list+[nums[i]])
        
        if not nums:
            return []
        res = []
        nums.sort()
        helper(nums, [])

        return res
