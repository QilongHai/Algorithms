class Empty(Exception):
    pass

class PriorityQueue:
    class _Element:
        def __init__(self, element, priority):
            self._element = element
            self._priority = priority

    def __init__(self):
        self._data = []
        self._size = 0

    def is_empty(self):
        return self._size == 0

    def enqueue(self, e, p):
        new = self._Element(e, p)
        if self.is_empty():
            self._data.append(new)
        i = self._size - 1
        while i >= 0:
            if self._data[i]._priority > new._priority:
                i -= 1
            else:
                break
        self._data.insert(i+1, new)
        self._size += 1

    def first(self):
        if self.is_empty():
            raise Empty('queue is empty')
        return self._data[-1]

    def deque(self):
        if self.is_empty():
            raise Empty('queue is empty')
        answer = self._data.pop()
        self._size -= 1
        return answer



