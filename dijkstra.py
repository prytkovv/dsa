import heapq as hq


def dijkstra(graph, source):
    # initialize
    predecessors = {v: None for v in graph}
    distances = {v: float('inf') for v in graph}
    distances[source] = 0
    # create heap queue
    queue = [(0, source)]
    while queue:
        # pop item with minimal distance
        current_distance, current_vertex = hq.heappop(queue)
        # find neighbours for item with minimal distance
        for vertex, distance in graph[current_vertex].items():
            tentative_distance = current_distance + distance
            # relax edges
            if tentative_distance < distances[vertex]:
                distances[vertex] = tentative_distance
                predecessors[vertex] = current_vertex
                hq.heappush(queue, (tentative_distance, vertex))
    return distances, predecessors


# graph = {
#     'A': {'B': 5, 'C': 2},
#     'B': {'D': 4, 'E': 2},
#     'C': {'E': 7, 'B': 8},
#     'D': {'E': 6, 'F': 3},
#     'E': {'F': 1},
#     'F': {}
# }
# dijkstra(graph, 'A')
