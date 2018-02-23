class GraphError(ValueError):
    pass

class Graph:
    def __init__(self, matrix=[], un_connect=0):
        vertex_num = len(matrix)
        for i in matrix:
            if len(i) != vertex_num:
                raise ValueError('the matrix is not a square matrix.')
        self._matrix = [self._out_edges(matrix[i], un_connect) for i in range(vertex_num)]
        self._vertex_num = vertex_num
        self._un_connect = un_connect

    def add_edge(self, vi, vj, value=1):
        """to do"""
        pass

    def get_edge(self, vi, vj):
        """to do"""
        pass

    def out_edges(self, vi):
        """to do"""
        pass

    @staticmethod
    def _out_edges(row, un_connect):
        edges = []
        for i in range(len(row)):
            if row[i] != un_connect:
                edges.append((i, row[i]))
        return edges
