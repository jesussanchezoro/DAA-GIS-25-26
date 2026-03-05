

def ap_rec(g, u, data):
    data['visited'][u] = True
    data['disc'][u] = data['time']
    data['low'][u] = data['time']
    data['time'] += 1
    children = 0
    for v in g[u]:
        if not data['visited'][v]:
            data['parent'][v] = u
            children += 1
            ap_rec(g, v, data)
            data['low'][u] = min(data['low'][u], data['low'][v])
            if data['parent'][u] == -1 and children > 1:
                data['points'].add(u)
            if data['parent'][u] != -1 and data['low'][v] >= data['disc'][u]:
                data['points'].add(u)
        elif v != data['parent'][u]:
            data['low'][u] = min(data['low'][v], data['disc'][v])


def ap(g):
    n = len(g)
    data = {}
    data['visited'] = [False] * n
    data['disc'] = [0x3f3f3f] * n
    data['low'] = [0x3f3f3f] * n
    data['parent'] = [-1] * n
    data['points'] = set()
    data['time'] = 0
    for i in range(n):
        if not data['visited'][i]:
            ap_rec(g, i, data)
    return data['points']


n,m = map(int, input().strip().split())
costs = []
g = []
for _ in range(n):
    cost = int(input().strip())
    costs.append(cost)
    g.append([])
for _ in range(m):
    a, b = map(int, input().strip().split())
    g[a].append(b)
    g[b].append(a)

points = ap(g)
cost = 0
for p in points:
    cost += costs[p]
print(cost)