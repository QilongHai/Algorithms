class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        x_stack = []
        y_stack = []
        while x:
            x_stack.append(x % 2)
            x >>= 1
        while y:
            y_stack.append(y % 2)
            y >>= 1
        if len(x_stack) < len(y_stack):
            for _ in range(len(y_stack) - len(x_stack)):
                x_stack.append(0)
        else:
            for _ in range(len(x_stack) - len(y_stack)):
                y_stack.append(0)
        count = 0
        for idx in range(len(x_stack)):
            if x_stack[idx] != y_stack[idx]:
                count += 1
        return count
