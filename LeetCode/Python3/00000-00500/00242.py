class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_new = sorted(s)
        t_new = sorted(t)
        if s_new == t_new:
            return True
        else:
            return False
