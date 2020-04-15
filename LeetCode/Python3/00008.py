class Solution:
    def myAtoi(self, s: str) -> int:
        if not s:
            return 0
        num_dict = dict()
        for i in range(10):
            num_dict[str(i)] = i
        index = 0
        length = len(s)
        while index < length and s[index] == ' ':
            index += 1
        if index >= length:
            return 0
        if s[index] not in num_dict and s[index] not in ['+', '-']:
            return 0

        s = s[index:]
        print(s)
        sign = 1 if s[0] != '-' else -1
        max_val = pow(2, 31) - 1 if sign == 1 else -pow(2, 31)
        res = 0
        if s[0] in ['+', '-']:
            s = s[1:]
        for i in s:
            if i in num_dict:
                res = res * 10 + num_dict[i]
                if sign == 1:
                    if res > max_val:
                        return max_val
                    else:
                        continue
                else:
                    if sign * res < max_val:
                        return max_val
                    else:
                        continue
            else:
                break
        return sign * res


class Automation:
    """
    state machine
                    ' '	    +/-	    number	    other
        start   	start	signed	in_number	end
        signed  	end	    end	    in_number	end
        in_number   end	    end	    in_number	end
        end     	end	    end	    end	        end
    """

    def __init__(self):
        self.state = 'start'
        self.ans = 0
        self.sign = 1
        self.table = {
            'start': ['start', 'signed', 'in_number', 'end'],
            'signed': ['end', 'end', 'in_number', 'end'],
            'in_number': ['end', 'end', 'in_number', 'end'],
            'end': ['end', 'end', 'end', 'end']
        }

    def get_col_index(self, char):
        if char.isspace():
            return 0
        elif char in ['+', '-']:
            return 1
        elif char.isdigit():
            return 2
        else:
            return 3

    def compute(self, char):
        self.state = self.table[self.state][self.get_col_index(char)]
        if self.state == 'signed':
            self.sign = 1 if char == '+' else -1
        elif self.state == 'in_number':
            self.ans = self.ans * 10 + int(char)
        else:
            pass


class SolutionTwo:
    def myAtoi(self, string: str) -> int:
        int_max = pow(2, 31) - 1
        int_min = -pow(2, 31)
        automation = Automation()

        for item in string:
            automation.compute(item)
        res = automation.sign * automation.ans
        if automation.sign == 1:
            return res if res < int_max else int_max
        else:
            return res if res > int_min else int_min
