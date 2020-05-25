class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num < 2:
            return True
        i = 2
        j = num // 2
        while i <= j:
            x = (i + j) // 2
            squared = x * x
            if squared == num:
                return True
            elif squared > num:
                j = x - 1
            else:
                i = x + 1
        return False