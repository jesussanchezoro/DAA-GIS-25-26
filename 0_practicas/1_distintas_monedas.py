import math


def cambiar_mon(mapa_cambios, mapa_conversiones, nombre, gasto):
    monedas = mapa_cambios[nombre]
    monedas_usadas = [0] * len(monedas)
    valor_euros = mapa_conversiones[nombre]
    gasto_inicial = gasto
    moneda_actual = 0
    while gasto > 0 and moneda_actual >= 0:
        monedas_usadas[moneda_actual] = gasto // monedas[moneda_actual]
        gasto %= monedas[moneda_actual]
        moneda_actual += 1
    return gasto_inicial * valor_euros, monedas_usadas

if __name__ == '__main__':
    n = int(input().strip())
    d = int(input().strip())
    mapa_cambios = {}
    mapa_conversiones = {}
    for _ in range(d):
        line = input().strip().split()
        nombre = line[0]
        cambio = float(line[1])
        cambios = list(map(int, line[2:]))
        mapa_cambios[nombre] = cambios
        mapa_conversiones[nombre] = cambio
    p = int(input().strip())
    dinero_ganado = n
    for i in range(p):
        line = input().strip().split()
        nombre = line[0]
        gasto = int(line[1])
        cambio_moneda, monedas = cambiar_mon(mapa_cambios, mapa_conversiones, nombre, gasto)
        dinero_ganado += math.ceil(cambio_moneda)
        print(f"Pedido {i+1} paga con", end=" ")
        for m in range(len(monedas)):
            if monedas[m] > 0:
                print((str(mapa_cambios[nombre][m])+" ")*monedas[m], end="")
        print()
    print(f"Dinero al final del dia: {dinero_ganado}")