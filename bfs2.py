# mark start node ad explored, add to queue
# while queue is not empty, dequeu item and try to explore it
# if item is not explored
# mark as explored and add to queue


def bfs(adj, s):
    queue = [s]
    visited = [s]
    while queue:
        u = queue.pop(0)
        for v in adj[u]:
            if v not in visited:
                visited.append(v)
                queue.append(v)
    return visited


# adj = {
#     'A': ['B', 'C'],
#     'B': ['D', 'E'],
#     'C': ['F'],
#     'D': [],
#     'E': ['F'],
#     'F': []
# }
# bfs(adj, 'B')
