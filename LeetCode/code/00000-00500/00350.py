from typing import List


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if len(nums1) < len(nums2):
            res = self.helper(nums1, nums2)
        else:
            res = self.helper(nums2, nums1)
        return res

    def helper(self, arr_a, arr_b):
        d = dict()
        for i in arr_a:
            d[i] = d.get(i, 0) + 1
        res = []
        for j in arr_b:
            if d.get(j, 0) > 0:
                res.append(j)
                d[j] -= 1
        return res
