import ctypes

class DynamicArray:
    def __init__(self):
        self._n = 0  # to count the elements
        self._capacity = 1  # default array capacity
        self._A = self._make_array(self._capacity)

    def __len__(self):
        return self._n

    def __getitem__(self, k):
        """Return element at index k."""
        if not 0 <= k < self._n:
            raise IndexError('invalid index')
        return self._A[k]

    def append(self, object):
        if self._n == self._capacity:  # no enough room to store the object
            self._resize(2 * self._capacity)
        self._A[self._n] = object
        self._n += 1

    def _resize(self, c):
        """Resize internal array to capacity c."""
        B = self._make_array(c)
        for i in range(self._n):
            B[i] = self._A[i]
        self._A = B
        self._capacity = c

    def _make_array(self, c):
        """Return new array with capacity c."""
        return (c * ctypes.py_object)()

    def insert(self, k, value):
        if self._n == self._capacity:
            self._resize(self._capacity * 2)
        for j in range(self._n, k, -1):
            self._A[j] = self._A[j-1]  # shift the part of right
        self._A[k] = value
        self._n += 1

    def remove(self, value):
        for k in range(self._n):
            if self.A[k] == value:
                for j in range(k, self._n-1):
                    self._A[j] = self._A[j+1]
                self._A[self._n-1] = None
                self._n -= 1
                return
        raise ValueError('value not found')

if __name__ == '__main__':
    A = DynamicArray()
    A.append(12)
    A.append(13)
    A.append(14)
    for i in A:
        print(i)
    print(len(A))
