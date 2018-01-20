def numero_tuneles(edificios):
    tuneles = 1
    sorted(edificios)
    limite_superior = edificios[0][1]
    for edificio in edificios:
        if edificio[0] > limite_superior:
            tuneles += 1
            limite_superior = edificio[1]

    return tuneles


if __name__ == '__main__':
    respuestas = []
    numero_casos = int(input())
    while numero_casos:
        edificios = []
        for i in range(numero_casos):
            edificios.append(tuple([int(x) for x in input().split(' ')]))
        respuestas.append(numero_tuneles(edificios))
        numero_casos = int(input())
    for respuesta in respuestas:
        print(respuesta)
