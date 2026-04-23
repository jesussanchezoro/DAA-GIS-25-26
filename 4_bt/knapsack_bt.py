import copy

def is_solution(sol, data):
    return sol['w'] + min(data['w']) > data['W']


def is_feasible(sol, data, i):
    return sol['w']+data['w'][i] <= data['W']


def add(sol, data, i):
    sol['o'][i] += 1
    sol['v'] += data['v'][i]
    sol['w'] += data['w'][i]

def remove(sol, data, i):
    sol['o'][i] -= 1
    sol['v'] -= data['v'][i]
    sol['w'] -= data['w'][i]


def knapsack_bt(data, sol, best_sol, k):
    if is_solution(sol, data):
        print(f"EXPLORADA -> {sol}")
        if sol['v'] > best_sol['v']:
            best_sol = copy.deepcopy(sol)
    else:
        for i in range(k, data['n']):
            if is_feasible(sol, data, i):
                add(sol, data, i)
                best_sol = knapsack_bt(data, sol, best_sol, i)
                remove(sol, data, i)
    return best_sol



data = {'n': 4, 'W': 8, 'w': [2,3,4,5], 'v':[3,5,6,10]}
sol = {'o': [0]*data['n'], 'v': 0, 'w': 0}
best_sol = {'o': [0]*data['n'], 'v': 0, 'w': 0}
best_sol = knapsack_bt(data, sol, best_sol, 0)
print(best_sol)