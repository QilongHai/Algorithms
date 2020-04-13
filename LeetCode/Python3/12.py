class Solution:
    def intToRoman(self, num: int) -> str:
        m_list = ['', 'M', 'MM', 'MMM']  # 千位
        c_list = ['', 'C', 'CC', 'CCC', 'CD', 'D', 'DC', 'DCC', 'DCCC', 'CM'] # 百位
        x_list = ['', 'X', 'XX', 'XXX', 'XL', 'L', 'LX', 'LXX', 'LXXX', 'XC'] # 十位
        i_list = ['', 'I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX'] # 个位

        return m_list[num//1000] + c_list[(num%1000)//100] + x_list[(num%100)//10] + i_list[num%10]


num = 1234
print(num, num//1000)
print(num, num%1000, (num%1000)//100)
print(num, num%100, (num%100)//10)
print(num, num%10)
