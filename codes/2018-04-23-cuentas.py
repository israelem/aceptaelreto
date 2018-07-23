if __name__ == '__main__':
    soluciones = []
    cantidad_movimientos = int(input())
    while cantidad_movimientos:
        lista_movimientos = [int(x) for x in input().split()]
        instantes = 0
        for corte in range(1, len(lista_movimientos)):
            if sum(lista_movimientos[:corte]) == sum(lista_movimientos[corte:]):
                instantes += 1
        soluciones.append(instantes)
        cantidad_movimientos = int(input())
    for solución in soluciones:
        print(solución)
