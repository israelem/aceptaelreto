if __name__ == '__main__':
    primero, numero_parejas = [int(x) for x in input().split()]
    bandada = [primero]
    soluciones = []
    parejas = [int(x) for x in input().split()]
    for pareja in zip(parejas[::2], parejas[1::2]):
        bandada += pareja
        bandada.sort()
        soluciones.append(bandada[len(bandada) // 2])
    final = input()
    for solucion in soluciones:
        print(solucion, end=' ')
