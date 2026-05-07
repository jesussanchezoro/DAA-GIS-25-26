


def is_solution(v, g):
    return v == len(g)


def is_feasible(g, sol, v, color):
    feasible = True
    i = 0
    while feasible and i < len(g[v]):
        adj = g[v][i]
        if adj < v:
            feasible = color != sol[adj]
        i += 1
    return feasible



def graph_coloring_bt(g, m, sol, v):
    if is_solution(v, g):
        is_sol = True
    else:
        is_sol = False
        color = 1
        while not is_sol and color <= m:
            if is_feasible(g, sol, v, color):
                sol[v] = color
                sol, is_sol = graph_coloring_bt(g, m, sol, v+1)
                if not is_sol:
                    sol[v] = -1
            color += 1
    return sol, is_sol


g = [
    [1, 2, 3],
    [0],
    [0, 3],
    [0, 2]
]
m = 3
start = 0
sol = [-1] * len(g)
sol, is_sol = graph_coloring_bt(g, m, sol, start)
if is_sol:
    print(sol)
else:
    print("La instancia del problema no tiene solucion")