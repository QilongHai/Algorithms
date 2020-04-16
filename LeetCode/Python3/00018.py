from typing import List


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        if not nums or len(nums) < 4:
            return []
        d = dict()
        n = len(nums)
        for i in range(n):
            for j in range(i + 1, n):
                tmp_sum = nums[i] + nums[j]
                if tmp_sum not in d:
                    d[tmp_sum] = [(i, j)]
                else:
                    d[tmp_sum].append((i, j))
        res = set()
        for k in d.keys():
            v = target - k
            if v in d:
                list_a = d[k]
                list_b = d[v]
                for (i, j) in list_a:
                    for (p, q) in list_b:
                        if i != p and i != q and j != p and j != q:
                            temp = [nums[i], nums[j], nums[p], nums[q]]
                            temp.sort()
                            res.add(tuple(temp))

        return list(res)


class SolutionTwo:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        if not nums or len(nums) < 4:
            return []
        n = len(nums)
        nums.sort()
        res = []
        for a in range(n - 3):
            if a > 0 and nums[a] == nums[a - 1]:
                continue
            for b in range(a + 1, n - 2):
                if b > a + 1 and nums[b] == nums[b - 1]:
                    continue
                c = b + 1
                d = n - 1
                while c < d:
                    tmp_sum = nums[a] + nums[b] + nums[c] + nums[d]
                    if tmp_sum == target:
                        res.append([nums[a], nums[b], nums[c], nums[d]])
                        while c < d and nums[c] == nums[c + 1]:
                            c += 1
                        while c < d and nums[d] == nums[d - 1]:
                            d -= 1
                        c += 1
                        d -= 1
                    elif tmp_sum < target:
                        c += 1
                    else:
                        d -= 1
        return res
