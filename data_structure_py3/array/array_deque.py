class Empty(Exception):
    pass

class Deque:
    def __init__(self):
        self._data = []
        self._n = 0
    def is_empty(self):
        return self._n == 0

    def add_front(self, e):
        self._data.append(e)
        self._n += 1

    def add_rear(self, e):
        self._data.insert(0, e)
        self._n += 1

    def remove_front(self):
        if self.is_empty():
            raise Empty('the deque is empty')
        self._n -= 1
        return self._data.pop()

    def remove_rear(self):
        if self.is_empty():
            raise Empty('the deque is empty')
        self._n -= 1
        return self._data.pop(0)

