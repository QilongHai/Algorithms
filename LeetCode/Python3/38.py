class Solution:
    def countAndSay(self, n: int) -> str:
        prev_person = '1'
        for i in range(1, n):
            next_person = ''
            num = prev_person[0]
            count = 1
            for j in range(1, len(prev_person)):
                if prev_person[j] == num:
                    count += 1
                else:
                    next_person += str(count) + num
                    num = prev_person[j]
                    count = 1
            next_person += str(count) + num
            prev_person = next_person
        return prev_person

# 链接：https://leetcode-cn.com/problems/count-and-say/solution/ji-su-jie-bu-di-gui-zhi-ji-lu-qian-hou-liang-ren-p
