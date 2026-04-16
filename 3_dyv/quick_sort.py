

def pivot(v, left, right):
    pivote = v[left]
    i = left+1
    while i < right and v[i] < pivote:
        i += 1
    j = right
    while j > left and v[j] > pivote:
        j -= 1
    while i < j:
        v[i], v[j] = v[j], v[i]
        i += 1
        while v[i] < pivote:
            i += 1
        j -= 1
        while v[j] > pivote:
            j -= 1
    v[left], v[j] = v[j], v[left]
    return j

def quick_sort(v, i, j):
    if i > j:
        return
    else:
        pivote = pivot(v, i, j)
        quick_sort(v, i, pivote - 1)
        quick_sort(v, pivote + 1, j)


# v = [4, 6, 4, 67, 4, 3, 4, 4, 65, 34, 5, 3, 5, 3]
v = [9, 4, 17, 21, 34, 6, 0, -5, 56, 14, 8, 43]
quick_sort(v, 0, len(v)-1)
print(v)