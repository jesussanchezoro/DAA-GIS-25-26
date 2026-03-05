






def dfs(g, disc, low, parent, time, ap, u):
    disc[u] = time[0]
    low[u] = time[0]
    time[0] += 1
    children = 0
    for v in g[u]:
        if disc[v] == -1:
            parent[v] = u
            children += 1
            dfs(g, disc, low, parent, time, ap, v)
            low[u] = min(low[u], low[v])
            if parent[u] != -1 and low[v] >= disc[u]:
                ap[u] = True
        elif v != parent[u]:
            low[u] = min(low[u], disc[v])
    if parent[u] == -1 and children > 1:
        ap[u] = True

def findArticulationPoints(g):
    v = len(g)
    disc = [-1] * v
    low = [-1] * v
    parent = [-1] * v
    ap = [False] * v
    time = [1]
    for i in range(v):
        if disc[i] == -1:
            dfs(g, disc, low, parent, time, ap, i)
    art_points = [node for node in range(v) if ap[node]]
    return art_points

g = [[1,2,3], [0,2,4,5], [0,1,5], [0, 6, 7], [1, 5], [1,2, 4], [3, 7], [3, 6]]

print(findArticulationPoints(g))