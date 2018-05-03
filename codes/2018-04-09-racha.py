if __name__ == '__main__':
    numero_casos = int(input())
    respuestas = []
    for _ in range(numero_casos):
        dias = int(input())
        registro = [int(x) for x in input().split()]
        ganancias = 0
        intervalo = []
        maximo = (0, [])
        dia = 0
        while dia < dias and -10000 < registro[dia] < 10000:
            if registro[dia] > 0 and ganancias == 0:
                intervalo.append(dia)
                ganancias = registro[dia]
            elif registro[dia] > 0:
                ganancias += registro[dia]
            elif ganancias > 0 and not intervalo == []:
                intervalo.append(dia - 1)
                if ganancias > maximo[0] or (ganancias == maximo[0] and
                                             intervalo[1] - intervalo[0] < maximo[1][1] - maximo[1][0]):
                    maximo = (ganancias, intervalo)
                intervalo = []
                ganancias = 0
            dia += 1
        if ganancias > 0 and not intervalo == []:
                intervalo.append(dia - 1)
                if ganancias > maximo[0] or (ganancias == maximo[0] and
                                             intervalo[1] - intervalo[0] < maximo[1][1] - maximo[1][0]):
                    maximo = (ganancias, intervalo)
        respuestas.append(maximo[1])
        for respuesta in respuestas:
            print(respuesta[0]+1, respuesta[1]+1)
