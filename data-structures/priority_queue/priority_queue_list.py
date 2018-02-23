class Empty(Exception):
    pass

class PriorityQueue:
    """Implementing priority queue using heap."""
    def __init__(self, e_list=[]):
        self._data = list(e_list)  # the top of heap is list(e_list)[0]
        if e_list:
            self.build_heap()

    def is_empty(self):
        return not self._data

    def peek(self):
        if self.is_empty():
            raise Empty('queue is empty')
        return self._data[0]

    def enqueue(self, e):
        self._data.append(None)  # add a dummy element
        self.sift_up(e, len(self._data)-1)

    def sift_up(self, e, last):
        data, i, j = self._data, last, (last-1) // 2
        while i > 0 and e < data[j]:
            data[i] = data[j]
            i, j = j, (j-1) // 2
        data[i] = e

    def dequeue(self):
        if self.is_empty():
            raise Empty('queue is empty')
        data = self._data
        value = data[0]
        e = data.pop()
        if len(data) > 0:
            self.sift_down(e, 0, len(data))
        return value

    def sift_down(self, e, start, end):
        data, i, j = self._data, start, start * 2 + 1
        while j < end:
            if j + 1 < end and data[j+1] < data[j]:
                j += 1
            if e < data[j]:
                break
            data[i] = data[j]
        data[i] = e

    def build_heap(self):
        end = len(self._data)
        for i in range(end // 2, -1, -1):
            self.sift_down(self._data[i], i, end)
