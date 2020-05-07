class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.data = []
        self.help = []

    def push(self, x: int) -> None:
        self.data.append(x)
        if not self.help:
            self.help.append(x)
        else:
            if x <= self.help[-1]:
                self.help.append(x)
            else:
                self.help.append(self.help[-1])

    def pop(self) -> None:
        if self.data:
            self.help.pop()
            return self.data.pop()

    def top(self) -> int:
        if self.data:
            return self.data[-1]

    def getMin(self) -> int:
        if self.help:
            return self.help[-1]