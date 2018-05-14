if __name__ == '__main__':
    numero_casos = int(input())
    respuestas = []
    for _ in range(numero_casos):
        dias = int(input())
        registro = [int(x) for x in input().split()]
        ganancias = []
        for inicio in range(dias):
            for fin in range(inicio, dias):
                ganancias.append((sum(registro[inicio:fin + 1]), [inicio + 1, fin + 1]))
        maximo = ganancias[0]
        for ganancia in ganancias[1:]:
            if ganancia[0] > maximo[0] or (ganancia[0] == maximo[0] and (ganancia[1][1] - ganancia[1][0]) <
                                           (maximo[1][1] - maximo[1][1])):
                maximo = ganancia
        respuestas.append(maximo[1])
        for respuesta in respuestas:
            print(respuesta[0], respuesta[1])
