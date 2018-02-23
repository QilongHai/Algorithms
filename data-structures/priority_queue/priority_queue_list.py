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

