class Solution:
    def myAtoi(self, s: str) -> int:
        if not s:
            return 0
        num_dict = dict()
        for i in range(10):
            num_dict[str(i)] = i
        index = 0
        length = len(s)
        while index < length and s[index] == ' ':
            index += 1
        if index >= length:
            return 0
        if s[index] not in num_dict and s[index] not in ['+', '-']:
            return 0

        s = s[index:]
        print(s)
        sign = 1 if s[0] != '-' else -1
        max_val = pow(2, 31) - 1 if sign == 1 else -pow(2, 31)
        res = 0
        if s[0] in ['+', '-']:
            s = s[1:]
        for i in s:
            if i in num_dict:
                res = res * 10 + num_dict[i]
                if sign == 1:
                    if res > max_val:
                        return max_val
                    else:
                        continue
                else:
                    if sign * res < max_val:
                        return max_val
                    else:
                        continue
            else:
                break
        return sign * res


s = Solution()
res = s.myAtoi(" ")
print(res)



