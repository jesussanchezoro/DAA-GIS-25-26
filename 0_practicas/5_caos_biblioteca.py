def count_and_merge(arr, temp_arr, left, mid, right):
    i = left
    j = mid + 1
    k = left
    inv_count = 0

    while i <= mid and j <= right:
        if arr[i] <= arr[j]:
            temp_arr[k] = arr[i]
            i += 1
        else:
            temp_arr[k] = arr[j]
            inv_count += (mid - i + 1)
            j += 1
        k += 1

    while i <= mid:
        temp_arr[k] = arr[i]
        i += 1
        k += 1
    while j <= right:
        temp_arr[k] = arr[j]
        j += 1
        k += 1

    for loop_k in range(left, right + 1):
        arr[loop_k] = temp_arr[loop_k]

    return inv_count


def solve_chaos(arr, temp_arr, left, right):
    inv_count = 0
    if left < right:
        mid = (left + right) // 2
        inv_count += solve_chaos(arr, temp_arr, left, mid)
        inv_count += solve_chaos(arr, temp_arr, mid + 1, right)
        inv_count += count_and_merge(arr, temp_arr, left, mid, right)
    
    return inv_count


if __name__ == "__main__":
    n = int(input().strip())
    global_chaos = 0
    for _ in range(n):
        arr = list(map(int, input().strip().split()))
        temp_arr = arr.copy()
        sol = solve_chaos(arr, temp_arr, 0, len(arr) - 1)
        print(sol)
        global_chaos += sol
    print(global_chaos)

'''

if __name__ == "__main__":
    for i in range(2, 12):
        with open("test"+str(i)+".in", 'r') as f:
            n = int(f.readline().strip())
            global_chaos = 0
            with open("test"+str(i)+".ans", 'w') as fo:
                for _ in range(n):
                    arr = list(map(int, f.readline().strip().split()))
                    temp_arr = arr.copy()
                    sol = solve_chaos(arr, temp_arr, 0, len(arr) - 1)
                    fo.write(str(sol)+"\n")
                    global_chaos += sol
                fo.write(str(global_chaos)+"\n")
'''