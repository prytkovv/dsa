visited = []


def dfs(adj, u):
    visited.append(u)
    for v in adj[u]:
        if v not in visited:
            dfs(adj, v)


# adj = {
#     'A': ['B', 'C'],
#     'B': ['D', 'E'],
#     'C': ['F'],
#     'D': [],
#     'E': ['F'],
#     'F': []
# }
# dfs(adj, 'A')

