class Empty(Exception):
    pass

class MyStack:
    def __init__(self):
        self._data = []
        self._size = 0

    def is_empty(self):
        return self._size == 0
    def push(self, e):
        self._data.append(e)
        self._size += 1

    def pop(self):
        if self.is_empty():
            raise Empty('stack is empty')
        answer = self._data.pop()
        self._size -= 1
        return answer

def dfs_graph(graph, vertex_start):
    vertex_num = graph.vertex_num()
    visited = [0] * vertex_num
    visited[vertex_start] = 1
    dfs_sequence = [vertex_start]  # record the sequence of traverse
    s = MyStack()
    s.push((0, graph.out_edges(vertex_start)))
    while not s.is_empty():
        i, edges = s.pop()
        if i < len(edges):
            vertex, edge = edges[i]
            s.push((i+1, edges))
            if not visited[vertex]:
                dfs_sequence.append(vertex)
                visited[vertex] = 1
                s.push((0, graph.out_edges(vertex)))
    return dfs_sequence

