from typing import List


class Solution:

    def merge_naive(self, nums1, nums2):
        res = []
        i = 0
        j = 0
        while i < len(nums1) and j < len(nums2):
            if nums1[i] < nums2[j]:
                res.append(nums1[i])
                i += 1
            else:
                res.append(nums2[j])
                j += 1
        while i < len(nums1):
            res.append(nums1[i])
            i += 1
        while j < len(nums2):
            res.append(nums2[j])
            j += 1
        return res

    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        nums1_copy = nums1[:m]
        i = 0
        j = 0
        nums1[:] = []
        while i < m and j < n:
            if nums1_copy[i] < nums2[j]:
                nums1.append(nums1_copy[i])
                i += 1
            else:
                nums1.append(nums2[j])
                j += 1
        if i < m:
            while i < m:
                nums1.append(nums1_copy[i])
                i += 1
        if j < n:
            while j < n:
                nums1.append(nums2[j])
                j += 1

    def merge_three(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        p1 = m - 1
        p2 = n - 1
        p = m + n - 1
        while p1 >= 0 and p2 >= 0:
            if nums1[p1] < nums2[p2]:
                nums1[p] = nums2[p2]
                p2 -= 1
            else:
                nums1[p] = nums1[p1]
                p1 -= 1
            p -= 1
        if p2 >= 0:  # or replace with: nums1[:p2 + 1] = nums2[:p2 + 1]
            while p2 >= 0:
                nums1[p] = nums2[p2]
                p2 -= 1
                p -= 1
