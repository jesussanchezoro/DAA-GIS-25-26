def binary_search(enemigos, q, ini, fin):
    if enemigos[0] > q:
        return -1
    elif ini == fin:
        return ini
    else:
        medio = (fin + ini) // 2
        if q >= enemigos[medio + 1]:
            return binary_search(enemigos, q, medio + 1, fin)
        else:
            return binary_search(enemigos, q, ini, medio)

def main():
    n = int(input().strip())
    enemigos = list(map(int, input().strip().split()))
    suma_puntos = []
    suma_puntos.append(enemigos[0])
    for i in range(1, n):
        suma_puntos.append(suma_puntos[i - 1] + enemigos[i])
    m = int(input().strip())
    for i in range(m):
        q = int(input().strip())
        ini = 0
        fin = n - 1
        pos = binary_search(enemigos, q, ini, fin)
        if (pos == -1):
            print(0, 0)
        else:
            print(pos + 1, suma_puntos[pos])



if __name__ == '__main__':
    main()
