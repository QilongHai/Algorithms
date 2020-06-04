from typing import List


class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        res = 0
        sum_k = 0
        target = k * threshold
        for i in range(k):
            sum_k += arr[i]
        tmp = sum_k - target
        if tmp >= 0:
            res += 1
        pos = k
        for i in range(len(arr) - k):
            tmp += arr[pos] - arr[i]
            if tmp >= 0:
                res += 1
            pos += 1
        return res
