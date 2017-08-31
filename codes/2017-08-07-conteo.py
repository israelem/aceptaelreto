if __name__ == '__main__':
    inicio, fin = [int(x) for x in input().split(' ')]
    respuestas = []
    while inicio != 0 and fin != 0:
        paginas = range(inicio, fin+1)
        sumatorio = sum([len(str(x)) for x in paginas])
        posicion = 0
        conteo = len(str(paginas[posicion]))
        while conteo + len(str(paginas[posicion])) < sumatorio // 2:
            conteo += len(str(paginas[posicion]))
            posicion += 1
        respuestas.append(paginas[posicion])
        inicio, fin = [int(x) for x in input().split(' ')]
    for x in respuestas:
        print(x)
