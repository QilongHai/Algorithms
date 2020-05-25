class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        if not ransomNote:
            return True
        count_dict = {}
        for c in ransomNote:
            count_dict[c] = count_dict.get(c, 0) + 1
        n = len(ransomNote)
        for c in magazine:
            if c in count_dict and count_dict[c] >= 1:
                count_dict[c] -= 1
                n -= 1
                if n == 0:
                    return True
        return False
