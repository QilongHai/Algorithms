from typing import List


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)
        for i in range(n):
            j = i
            remain = gas[i]
            while remain - cost[j] >= 0:
                remain = remain - cost[j] + gas[(j + 1) % n]
                j = (j + 1) % n
                if j == i:
                    return i
        return -1
