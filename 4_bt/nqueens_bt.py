

def print_board(sol):
    N = len(sol)

    header = "  " + " ".join(str(i) for i in range(N))
    print(header)
    print(" +" + "--" * N + "-")

    for i in range(N):
        row_str = str(i) + "| "
        for j in range(N):
            row_str += "Q " if j == sol[i] else ". "
        print(row_str)


def is_solution(sol, row):
    return row == len(sol)


def is_feasible(sol, row, col):
    feasible = True
    i = 1
    while feasible and i <= row:
        feasible_col = sol[row-i] != col
        feasible_diag_45 = sol[row-i] != col-i
        feasible_diag_135 = sol[row-i] != col+i
        feasible = feasible_col and feasible_diag_45 and feasible_diag_135
        i += 1
    return feasible


def n_queens_bt(sol, n, row, sol_found):
    if is_solution(sol, row):
        sol_found = True
        print(sol)
    else:
        col = 0
        while not sol_found and col < n:
            if is_feasible(sol, row, col):
                sol[row] = col
                sol, sol_found = n_queens_bt(sol, n, row+1, sol_found)
                if not sol_found:
                    sol[row] = -1
            col += 1
    return sol, sol_found


n = 20
sol = [-1] * n
sol = n_queens_bt(sol, n, 0, False)
if sol[1]:
    print_board(sol[0])