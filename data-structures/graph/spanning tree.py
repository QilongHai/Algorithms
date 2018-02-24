def dfs_spanning_forest(graph):
    vertex_num = graph.vertex_num()
    span_forest = [None] * vertex_num

    def dfs(graph, v):
        nonlocal span_forest
        for u, w in graph.out_edges(v):
            if span_forest[u] is None:
                span_forest[u] = (u, w)
                dfs(graph, u)

    for v in range(vertex_num):
        if span_forest[v] is None:
            span_forest[v] =  (v, 0)
            dfs(graph, v)

    return span_forest