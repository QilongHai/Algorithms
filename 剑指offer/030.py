class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.data = []
        self.help = []

    def push(self, x: int) -> None:
        self.data.append(x)
        if self.help:
            if x < self.help[-1]:
                self.help.append(x)
            else:
                self.help.append(self.help[-1])
        else:
            self.help.append(x)

    def pop(self) -> None:
        if self.help:
            self.help.pop()
        if self.data:
            return self.data.pop()

    def top(self) -> int:
        if self.data:
            return self.data[-1]

    def min(self) -> int:
        if self.help:
            return self.help[-1]
        pass

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.min()
