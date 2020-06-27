class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for item in tokens:
            if item.isdigit() or (item[0] == '-' and item[1:].isdigit()):
                stack.append(int(item))
            elif item in ['+', '-', '*', '/']:
                if len(stack) >= 2:
                    a = stack.pop()
                    b = stack.pop()
                    if item == '+':
                        val = a + b
                    elif item == '-':
                        val = b - a
                    elif item == '*':
                        val = a * b
                    elif item == '/':
                        if (a > 0 and b < 0) or (a < 0 and b > 0) :
                            val = -(abs(b) // abs(a))
                        elif a == 0:
                            return ValueError('divid is zero')
                        else:
                            val = b // a
                    stack.append(val)
                else:
                    return Exception('invalid RPN expression')
        return stack[-1]