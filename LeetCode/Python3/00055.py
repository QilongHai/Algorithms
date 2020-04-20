# class Solution:
#     def canJump(self, nums: List[int]) -> bool:
#         k = 0
#         for i in range(len(nums)):
#             if i > k:
#                 return False
#             k = max(k, i+nums[i])
#         return True

class Solution:
    def canJump(self, nums) :
        max_i = 0       #初始化当前能到达最远的位置
        for i, jump in enumerate(nums):   #i为当前位置，jump是当前位置的跳数
            if max_i >= i and i+jump > max_i:  #如果当前位置能到达，并且当前位置+跳数>最远位置  
                max_i = i+jump  #更新最远能到达位置
        return max_i >= i

# 作者：mo-lan-4
# 链接：https://leetcode-cn.com/problems/jump-game/solution/pythonji-bai-97kan-bu-dong-ni-chui-wo-by-mo-lan-4/
