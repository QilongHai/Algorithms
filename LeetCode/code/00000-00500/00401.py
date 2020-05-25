from typing import List


class Solution:
    def readBinaryWatch(self, num: int) -> List[str]:
        if num < 0 or num > 10:
            return []
        res = []
        for i in range(num + 1):
            j = num - i
            if i > 3 or j > 5:
                continue
            hour = self.hours(i)
            minute = self.minutes(j)
            for a in hour:
                for b in minute:
                    res.append(a + ':' + b)
        return res

    def hours(self, num):
        res = []
        if num == 0:
            res = ['0']
        elif num == 1:
            res = ['1', '2', '4', '8']
        elif num == 2:
            res = ['3', '5', '9', '6', '10']
        elif num == 3:
            res = ['7', '11']
        return res

    def minutes(self, num):
        res = []
        if num == 0:
            res = ['00']
        elif num == 1:
            res = ['01', '02', '04', '08', '16', '32']
        elif num == 2:
            res = ['03', '05', '09', '17', '33', '06', '10', '18', '34', '12', '20', '36', '24', '40', '48']
        elif num == 3:
            res = ['07', '11', '19', '35', '13', '21', '37', '25', '41', '49', '14', '22', '38', '26', '42', '50', '28',
                   '44', '52', '56']
        elif num == 4:
            res = ['58', '54', '46', '30', '57', '53', '45', '29', '51', '43', '27', '39', '23', '15']
        elif num == 5:
            res = ['59', '55', '47', '31']
        return res


class SolutionTwo:
    def readBinaryWatch(self, num: int) -> List[str]:
        def count_one(tmp):
            return bin(tmp).count('1')

        dic = {i: count_one(i) for i in range(60)}
        res = []
        for i in range(12):
            for j in range(60):
                if dic[i] + dic[j] == num:
                    hour = str(i)
                    minute = str(j) if j > 9 else '0' + str(j)
                    res.append(hour + ":" + minute)
        return res
