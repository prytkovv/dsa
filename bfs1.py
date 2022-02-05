def bfs(adj, s):
    levels = {s: 0}
    parents = {s: None}
    i = 1
    frontier = [s]
    while frontier:
        next = []
        for u in frontier:
            for v in adj[u]:
                if v not in levels:
                    levels[v] = i
                    parents[v] = u
                    next.append(v)
        frontier = next
        i += 1


# graph = {
#   'A': ['B', 'C'],
#   'B': ['D', 'E'],
#   'C': ['F'],
#   'D': [],
#   'E': ['F'],
#   'F': []
# }
# bfs(graph, 'A')
