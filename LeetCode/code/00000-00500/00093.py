from typing import List


class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        n = len(s)
        res = []
        for i in range(3):
            for j in range(i+1, i+4):
                for k in range(j+1, j+4):
                    if i < n and j < n and k < n:
                        a = s[:i+1]
                        b = s[i+1:j+1]
                        c = s[j+1:k+1]
                        d = s[k+1:]
                        print([i, j, k], [a, b, c, d])
                        if all(map(self.is_valid_ip, [a, b, c, d])):
                            res.append('.'.join([a, b, c, d]))
        return res

    def is_valid_ip(self, string):
        if not string:
            return False
        elif string[0] == '0' and len(string) > 1:
            return False
        elif int(string) > 255:
            return False
        else:
            return True


if __name__ == '__main__':
    pass
    obj = Solution()
    s = "25525511135"
    obj.restoreIpAddresses(s)

