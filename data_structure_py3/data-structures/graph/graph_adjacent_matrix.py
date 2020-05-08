class GraphError(ValueError):
    pass

class Graph:
    def __init__(self, matrix, un_connect=0):
        vertex_num = len(matrix)
        for i in matrix:
            if len(i) != vertex_num:  # to check the matrix is square matrix
                raise ValueError('Argument for Graph.')
        self._matrix = [matrix[i][:] for i in range(vertex_num)]  # to copy the matrix
        self._un_connect = un_connect
        self._vertex_num = vertex_num

    def vertex_num(self):
        return self._vertex_num

    def _invalid(self, v):
        return v > self._vertex_num or v < 0

    def add_vertex(self):
        """add a row and add a element for every row.
        to do"""
        pass

    def add_edge(self, vi, vj, value=1):
        if self._invalid(vi) or self._invalid(vj):
            raise GraphError(str(vi) + ' or ' + str(vj) + 'is not a valid vertex.')
        self._matrix[vi][vj] = value

    def get_edge(self, vi, vj):
        if self._invalid(vi) or self._invalid(vj):
            raise GraphError(str(vi) + ' or ' + str(vj) + 'is not a valid vertex.')
        return self._matrix[vi][vj]

    def out_edges(self, vi):
        if self._invalid(vi):
            raise  GraphError(str(vi) + ' is not a valid vertex.')
        return self._out_edges(self._matrix[vi], self._un_connect)

    @staticmethod
    def _out_edges(row, un_connect):
        edges = []
        for i in range(len(row)):
            if row[i] != un_connect:
                edges.append((i, row[i]))
        return edges
