def kruskal(graph):
    vertex_num = graph.vertex_num()
    reps = [i for i in range(vertex_num)]
    mst, edges = [], []
    for vi in range(vertex_num):
        for v, w in graph.out_edges(vi):
            edges.append((w, vi, v))
    edges.sort()
    for w, vi, vj in edges:
        if reps[vi] != reps[vj]:
            mst.append(((vi, vj), w))
            if len(mst) == vertex_num - 1:
                break
            rep, orep = reps[vi], reps[vj]
            for i in range(vertex_num):
                if reps[i] == orep:
                    reps[i] = rep
    return mst


def prime(graph):
    """to do"""
    pass