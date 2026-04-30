import copy


def is_sol(lab, r, c):
    return r == len(lab)-1 and c == len(lab[0])-1


def is_better(lab, best):
    n = len(lab)-1
    m = len(lab[0])-1
    return lab[n][m] < best[n][m]


def is_feasible(lab, r, c):
    return 0 <= r < len(lab) and 0 <= c < len(lab[0]) and lab[r][c] == 0


def print_lab(lab):
    for i in range(len(lab)):
        for j in range(len(lab[0])):
            print("|", end="")
            if lab[i][j] == -1:
                print(" *", end="\t")
            elif lab[i][j] == 0:
                print("  ", end="\t")
            else:
                print(f"{lab[i][j]:2}", end="\t")
        print("|")
        print("-"*4*len(lab))


def labyrinth(lab, best, r, c, k):
    if is_sol(lab, r, c):
        if is_better(lab, best):
            best = copy.deepcopy(lab)
    else:
        dir = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        for d in dir:
            new_r = r + d[0]
            new_c = c + d[1]
            if is_feasible(lab, new_r, new_c):
                lab[new_r][new_c] = k
                best = labyrinth(lab, best, new_r, new_c, k+1)
                lab[new_r][new_c] = 0
    return best



# lab = [
#     [0, 0, -1, 0, 0, 0, 0, -1, 0, 0],
#     [-1, 0, -1, 0, 0, -1, -1, 0, -1, 0],
#     [0, 0, 0, 0, 0, 0, -1, 0, -1, 0],
#     [0, -1, 0, 0, -1, -1, -1, 0, 0, 0],
#     [0, 0, -1, -1, 0, 0, 0, -1, 0, 0],
#     [0, 0, 0, 0, 0, -1, 0, -1, 0, 0],
#     [-1, 0, 0, -1, -1, 0, 0, -1, 0, -1],
#     [0, -1, -1, 0, 0, 0, 0, 0, -1, -1],
#     [-1, 0, 0, 0, 0, -1, 0, -1, -1, 0],
#     [0, 0, -1, 0, -1, -1, 0, 0, 0, 0]
# ]

lab = [
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
]


k = 1
lab[0][0] = k
best = copy.deepcopy(lab)
best[len(best)-1][len(best[0])-1] = 0x3f3f3f3f
best = labyrinth(lab, best, 0, 0, k+1)
print_lab(best)