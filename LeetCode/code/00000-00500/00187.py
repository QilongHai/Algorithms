from typing import List


class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        # """编写一个函数来查找子串，这个子串长度为10，在原字符串中出现超过一次。"""
        n = len(s)
        seen = set()
        res = set()
        for i in range(n - 10 + 1):  # 相当于拿一把长为10的尺子从左移动到最右
            if s[i:i + 10] not in seen:
                seen.add(s[i:i + 10])
            else:
                res.add(s[i:i + 10])
        return list(res)
