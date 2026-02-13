
def get_best_item(candidates, profit):
    best_item = -1
    best_profit = -1
    for c in candidates:
        if profit[c] > best_profit:
            best_profit = profit[c]
            best_item = c
    return best_item

def greedy_schedule(profit, deadline):
    n = len(profit)
    candidates = set()
    for i in range(n):
        candidates.add(i)
    last_date = max(deadline)
    sol = [-1] * (last_date+1)
    j = 0
    while candidates and j <= last_date:
        best = get_best_item(candidates, profit)
        candidates.remove(best)
        i = deadline[best]
        found = False
        while i > 0 and not found:
            if sol[i] == -1:
                sol[i] = best
                found = True
            i -= 1
        j += 1
    return sol


profit = [50, 10, 15, 30]
deadline = [2, 1, 2, 1]
schedule = greedy_schedule(profit, deadline)
print(schedule)