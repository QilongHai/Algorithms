class Solution:
    def reverseVowels(self, s: str) -> str:
        if not s:
            return s
        if len(s) < 2:
            return s
        vowel_dict = dict()
        for char in ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']:
            vowel_dict[char] = 0
        i = 0
        j = len(s) - 1
        res = ['' for _ in range(len(s))]
        while i <= j:
            if s[i] not in vowel_dict and s[j] not in vowel_dict:
                res[i] = s[i]
                res[j] = s[j]
                i += 1
                j -= 1
            elif s[i] in vowel_dict and s[j] in vowel_dict:
                res[i] = s[j]
                res[j] = s[i]
                i += 1
                j -= 1
            elif s[i] not in vowel_dict and s[j] in vowel_dict:
                res[i] = s[i]
                i += 1
            elif s[i] in vowel_dict and s[j] not in vowel_dict:
                res[j] = s[j]
                j -= 1
        return ''.join(res)