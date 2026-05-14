import copy

def is_sol(sol, max_ego):
    return sol['ego'] >= max_ego

def is_feasible(o, sol, max_ego):
    return sol['ego'] < max_ego and o not in sol['selected']


def bt(players, sol, best_sol, max_ego, k):
    if is_sol(sol, max_ego):
        if sol['skill'] > best_sol['skill']:
            best_sol = copy.deepcopy(sol)
    else:
        for i in range(k, len(players)):
            o = players[i]
            if is_feasible(o, sol, max_ego):
                sol['selected'].add(o)
                sol['ego'] += o[1]
                sol['skill'] += o[2]
                best_sol = bt(players, sol, best_sol, max_ego, k+1)
                sol['selected'].remove(o)
                sol['ego'] -= o[1]
                sol['skill'] -= o[2]
    return best_sol





n_players, max_ego = map(int, input().strip().split())
players = []
for _ in range(n_players):
    name, ego, skill = input().strip().split()
    players.append((name, int(ego), int(skill)))
team = dict()
team['selected'] = set()
team['ego'] = 0
team['skill'] = 0
best_team = dict()
best_team['selected'] = set()
best_team['ego'] = 0
best_team['skill'] = 0
best_team = bt(players, team, best_team, max_ego, 0)
print(f"{best_team['skill']} {best_team['ego']-max_ego}")
selected = sorted(list(best_team['selected']))
for p in selected:
    print(p[0])