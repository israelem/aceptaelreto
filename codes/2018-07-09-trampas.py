def hay_camino(inicio, fin, longitud, dado, saltos):
    if inicio == fin:
        return True
    elif not longitud:
        return False
    else:
        tirada = 1
        camino = False
        while tirada <= dado and not camino:
            siguiente = inicio + tirada
            if siguiente in saltos:
                siguiente = saltos[siguiente]
            camino = hay_camino(siguiente, fin, longitud - 1, dado, saltos)
            tirada += 1
        return camino

if __name__ == '__main__':
    soluciones = []
    tablero, dado, serpientes, escaleras = [int(x) for x in input().split()]
    while tablero and dado and serpientes and escaleras:
        saltos = dict()
        for _ in range(serpientes + escaleras):
            inicio, fin = [int(x) for x in input().split()]
            saltos[inicio] = fin
        camino = False
        longitud = 0
        while(not camino):
            longitud += 1
            camino = hay_camino(1, tablero**2, longitud, dado, saltos)
        soluciones.append(longitud)
        tablero, dado, serpientes, escaleras = [int(x) for x in input().split()]
    for solución in soluciones:
        print(solución)
