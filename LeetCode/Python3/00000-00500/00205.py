class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        else:
            d_s = dict()
            d_t = dict()
            for i in range(len(s)):
                if s[i] not in d_s and t[i] not in d_t:
                    d_s[s[i]] = i
                    d_t[t[i]] = i
                elif s[i] not in d_s and t[i] in d_t:
                    return False
                elif s[i] in d_s and t[i] not in d_t:
                    return False
                elif d_s.get(s[i]) != d_t.get(t[i]):
                    return False
            return True