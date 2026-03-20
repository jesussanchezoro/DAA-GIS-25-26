
def select_min(distances, visited):
    next_node = 0
    min_dist = 0x3f3f3f3f
    for i in range(1, len(distances)):
        if not visited[i] and distances[i] < min_dist:
            next_node = i
            min_dist = distances[i]
    return next_node


def dijkstra(g, start):
    n = len(g)-1
    distances = [0x3f3f3f3f] * (n+1)
    visited = [False] * (n+1)
    distances[start] = 0
    visited[start] = True
    for src, dst, w in g[start]:
        distances[dst] = w
    for _ in range(2, n+1):
        next_node = select_min(distances, visited)
        visited[next_node] = True
        for src, dst, w in g[next_node]:
            distances[dst] = min(distances[dst], distances[src]+w)
    return distances




g = [
    [],
    [(1,2,5),(1,4,3)],
    [(2,5,1)],
    [],
    [(4,2,1),(4,3,11),(4,5,6)],
    [(5,3,1)]
]
start = 1
sol = dijkstra(g, start)
print(sol[1:])