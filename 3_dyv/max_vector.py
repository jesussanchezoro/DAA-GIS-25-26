import random
import time

def max_vector_trad(v):
    m = v[0]
    for i in range(1, len(v)):
        m = max(m, v[i])
    return m


def max_vector_dyv(v):
    if len(v) == 1:
        # return v[0]
        return max_vector_trad(v)
    else:
        mitad = len(v) // 2
        izq = max_vector_dyv(v[0 : mitad])
        der = max_vector_dyv(v[mitad : len(v)])
        return max(izq, der)


def max_vector_dyv_efficient(v, l, h):
    if l == h:
        return v[l]
    else:
        mitad = (l + h) // 2
        izq = max_vector_dyv_efficient(v, l, mitad)
        der = max_vector_dyv_efficient(v, mitad+1, h)
        return max(izq, der)


nVals = [10, 100, 1000, 10000, 100000, 1000000, 10000000]
for n in nVals:
    print(n, end=" ")
    v = random.sample(range(n*10), n)
    ini = time.time()
    mt = max_vector_trad(v)
    print(time.time()-ini, end=" ")
    ini = time.time()
    mdyv = max_vector_dyv(v)
    print(time.time()-ini, end=" ")
    ini = time.time()
    mdyv_eff = max_vector_dyv_efficient(v, 0, len(v)-1)
    print(time.time() - ini)
