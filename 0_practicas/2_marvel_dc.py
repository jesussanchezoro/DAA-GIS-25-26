from collections import deque

def bfsAux(g, visited, v, type, types):
    q = deque()
    visited[v] = True
    q.append(v)
    while q:
        aux = q.popleft()
        for adj in g[aux]:
            if not visited[adj] and type == types[adj]:
                q.append(adj)
                visited[adj] = True

def bfs(g, type, types):
    n = len(g)
    visited = [False] * n
    ncc = 0
    for v in range(0, n):
        if not visited[v] and type == types[v]:
            bfsAux(g, visited, v, type, types)
            ncc += 1
    return ncc

if __name__ == '__main__':
    n, m, type = input().strip().split()
    n=int(n)
    m=int(m)
    g = []
    types = []
    for _ in range(n):
        g.append([])
        idType = input().strip()
        types.append(idType)
    for _ in range(m):
        a, b = map(int, input().strip().split())
        g[a].append(b)
        g[b].append(a)
    ncc = bfs(g, type, types)
    print(ncc)