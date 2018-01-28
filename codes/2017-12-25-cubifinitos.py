def cubifinito(numero):
    suma = sum([int(x) ** 3 for x in str(numero)])
    anterior = 0
    respuesta = str(numero)
    while suma != 1 and anterior != suma:
        anterior = suma
        suma = sum([int(x) ** 3 for x in str(suma)])
        respuesta += ' -> ' + str(suma)
    if suma == 1:
        respuesta += ' -> cubifinito.'
    else:
        respuesta += ' -> ' + str(suma) + ' -> no cubifinito.'
    return respuesta

if __name__ == '__main__':
    respuestas = []
    numero = int(input())
    while numero != 0:
        respuestas.append(cubifinito(numero))
        numero = int(input())
    for respuesta in respuestas:
        print(respuesta)
