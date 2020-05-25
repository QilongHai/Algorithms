class Solution:
    def wordPattern(self, pattern: str, string: str) -> bool:
        if len(pattern) != len(string.strip().split()):
            return False

        d_pattern = dict()
        d_string = dict()
        idx = 0
        for p, s in zip(pattern, string.strip().split()):
            if p not in d_pattern and s not in d_string:
                d_pattern[p] = idx
                d_string[s] = idx
            elif p in d_pattern and s in d_string:
                if d_pattern[p] != d_string[s]:
                    return False
                else:
                    pass
            else:
                return False
            idx += 1
        return True
