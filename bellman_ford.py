class NegativeCycleException(Exception):
    pass


def bellman_ford(vertices, edges, source):
    # initialize
    predecessors = {v: None for v in vertices}
    distances = {v: float('inf') for v in vertices}
    distances[source] = 0
    # The outer loop is needed because the longest shortest path from source to destination will be N - 1
    # in case of the linear graph, where N is the number of the nodes in the graph.
    # For more information visit (Isaac_Zhu answer)
    # https://stackoverflow.com/questions/49263065/why-need-node-number-1-iterations-in-bellman-ford-algorithm-to-find-shortest
    for _ in range(len(vertices) - 1):
        for u, v, w in edges:
            # relax edges
            if distances[u] + w < distances[v]:
                distances[v] = distances[u] + w
                predecessors[v] = u
    # check for negative weigh cycles
    for u, v, w in edges:
        if distances[u] + w < distances[v]:
            raise NegativeCycleException('Graph contains a negative-weight cycle')
    return distances, predecessors


# vertices = ['A', 'B', 'C', 'D', 'E']
# edges = [
#     ('A', 'B', -1),
#     ('A', 'C', 4),
#     ('B', 'C', 3),
#     ('B', 'D', 2),
#     ('B', 'E', 2),
#     ('D', 'C', 5),
#     ('D', 'B', 1),
#     ('E', 'D', -3),
# ]
# bellman_ford(vertices, edges, 'E')
