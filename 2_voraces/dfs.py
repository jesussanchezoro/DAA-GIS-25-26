

def dfs_rec(v, g, visited):
    visited.add(v)
    print(f"Visiting node {v}")
    for u in g[v]:
        if u not in visited:
            dfs_rec(u, g, visited)


def dfs(g):
    n = len(g)-1
    visited = set()
    for v in range(1, n+1):
        if v not in visited:
            dfs_rec(v, g, visited)


g = [
    [],
    [2, 4, 8],
    [1, 3, 4],
    [2, 4, 5],
    [1, 2, 3, 7],
    [3, 6],
    [5, 7],
    [4, 6, 9],
    [1, 9],
    [7, 8]
]

dfs(g)