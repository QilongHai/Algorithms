from typing import List


class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        if len(pushed) != len(popped):
            return False
        stack = []
        idx = 0
        for item in pushed:
            stack.append(item)
            while stack and stack[-1] == item:
                stack.pop()
                idx += 1
        return len(stack) == 0
