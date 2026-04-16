

def binary_search(v, number, low, high):
    if low > high:
        return low
    else:
        mid = (low + high) // 2
        if number == v[mid]:
            return mid
        if number < v[mid]:
            return binary_search(v, number, low, mid-1)
        else:
            return binary_search(v, number, mid+1, high)


v = [1, 3, 3, 5, 6, 7, 9]
number = 0
pos = binary_search(v, number, 0, len(v)-1)
if pos >= 0:
    print(pos)
else:
    print(f"No esta, pero deberia estar despues de {v[-pos-1]}")