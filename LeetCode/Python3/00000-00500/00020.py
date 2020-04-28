class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        d = {')': '(',
             '}': '{',
             ']': '['}
        for char in s:
            if char in ['(', '{', '[']:
                stack.append(char)
            elif char in d:
                if stack and stack[-1] == d[char]:
                    stack.pop()
                else:
                    return False
            else:
                print(char)
        return len(stack) == 0
