def calcular_primero(niños, paso):
    lista = list(range(niños))
    indice = 0
    tamaño_lista = len(lista)
    while tamaño_lista > 1:
        indice = (indice + paso) % tamaño_lista
        del lista[indice]
        tamaño_lista -= 1
    return lista[0] + 1

if __name__ == '__main__':
    respuestas = []
    niños, paso = [int(x) for x in input().split(' ')]
    while niños != 0 and paso != 0:
        respuestas.append(calcular_primero(niños, paso))
        niños, paso = [int(x) for x in input().split(' ')]
    for respuesta in respuestas:
        print(respuesta)
