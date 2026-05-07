
def is_sol(g, sol, v):
    return len(sol) == len(g) + 1 and sol[0] == v


def is_feasible(v, sol, n):
    return v not in sol or (v == sol[0] and len(sol) == n)


def hamiltonian_cycle_bt(g, v, sol):
    if is_sol(g, sol, v):
        print(sol)
    else:
        for adj in g[v]:
            if is_feasible(adj, sol, len(g)):
                sol.append(adj)
                hamiltonian_cycle_bt(g, adj, sol)
                sol.pop()


g = [
    [1, 2, 3],
    [0, 2, 4, 5],
    [0, 1, 3, 5, 6],
    [0, 2, 6, 7],
    [1, 5],
    [1, 2, 4, 6],
    [2, 3, 5, 7],
    [3, 6]
]

start = 0
sol = [start]
hamiltonian_cycle_bt(g, start, sol)