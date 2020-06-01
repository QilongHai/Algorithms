class Solution:
    def isNumber(self, s: str) -> bool:
        float(s)
        s = s.strip()
        met_dot = False
        met_e = False
        met_digit = False
        for idx, char in enumerate(s):
            if char in ('+', '-'):
                if idx > 0 and s[idx - 1] not in ['E', 'e']:
                    return False
            elif char == '.':
                if met_dot or met_e:
                    return False
                met_dot = True
            elif char == 'e' or char == 'E':
                if met_e or not met_digit:
                    return False
                met_e, met_digit = True, False  # e后必须接，所以这时重置met_digit为False,以免e为最后一个char
            elif char.isdigit():
                met_digit = True
            else:
                return False
        return met_digit


class SolutionTwo:
    def isNumber(self, s: str) -> bool:
        automation = Automation()
        s = s.strip()
        for i in s:
            automation.compute(i)
        if automation.state == 'end':
            return False
        if automation.state == 'num':
            return True


class Automation:
    """
    state machine
                    ' '	    +/-	    num     dot     exp	    other
        blank   	blank	signed	num	    end     end     end
        signed  	end	    end	    num	    end     end     end
        num         end	    end	    num	    dot     exp     end
        dot         end     end     num     end     end     end
        exp         end     end     num     end     end     end
        end     	end	    end	    end	    end     end     end
    """

    def __init__(self):
        self.state = 'blank'
        self.tables = {'blank': ['blank', 'signed', 'num', 'end', 'end', 'end'],
                       'signed': ['end', 'end', 'num', 'end', 'end', 'end'],
                       'num': ['end', 'end', 'num', 'dot', 'exp', 'end'],
                       'dot': ['end', 'end', 'num', 'end', 'end', 'end'],
                       'exp': ['end', 'end', 'num', 'end', 'end', 'end'],
                       'end': ['end', 'end', 'end', 'end', 'end', 'end']
                       }

    def get_col(self, cur_str):
        if cur_str.isspace():
            return 0
        elif cur_str in ['+', '-']:
            return 1
        elif cur_str.isdigit():
            return 2
        elif cur_str == '.':
            return 3
        elif cur_str in ['E', 'e']:
            return 4
        else:
            return 5

    def compute(self, char):
        self.state = self.tables[self.state][self.get_col(char)]
