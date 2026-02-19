
def get_best_item(candidates, v, w):
    best_item = 0
    best_ratio = -1
    for c in candidates:
        ratio = v[c] / w[c]
        if ratio > best_ratio:
            best_item = c
            best_ratio = ratio
    return best_item


def greedy_knapsack(v, w, W):
    candidates = set()
    n = len(v)
    for i in range(n):
        candidates.add(i)
    sol = [0] * n
    weight = 0
    while candidates and weight < W:
        best = get_best_item(candidates, v, w)
        candidates.remove(best)
        if w[best] + weight <= W:
            sol[best] = 1
            weight += w[best]
        else:
            sol[best] = (W-weight) / w[best]
            weight = W
    return sol


v = [20, 30, 66, 40, 60]
w = [10, 20, 30, 40, 50]
W = 100

sol = greedy_knapsack(v, w, W)
print(sol)