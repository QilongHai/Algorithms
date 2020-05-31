from typing import List

class Solution:
    def minArray(self, numbers: List[int]) -> int:
        i = 0
        j = len(numbers) - 1
        while i <= j:
            mid = i + (j - i) // 2
            if numbers[mid] < numbers[j]:
                j = mid
            elif numbers[mid] > numbers[j]:
                i = mid + 1
            else:
                j -= 1
        return numbers[i]