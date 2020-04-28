from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        if digits[-1] <= 8:  # 个位小于等于8，直接加一
            digits[-1] += 1
            return digits
        else:
            carry = 1  # 加一可以看成进位的初始值为一
            stack = []  # 用栈来存放每一位的值
            for i in digits[::-1]:
                tmp_val = i + carry
                cur_val = tmp_val % 10
                carry = tmp_val // 10
                stack.append(cur_val)
            if carry > 0:  # 处理溢出
                stack.append(carry)

            return stack[::-1]
