respuestas = []
numero_calculos = int(input())
for x in range(numero_calculos):
    respuesta = ''
    calculo = [x for x in input().split()]
    resultado = int(calculo[0])
    calculo = calculo[1:len(calculo) - 1]
    for signo, numero in zip(calculo[::2], calculo[1::2]):
        if signo == '+':
            resultado += int(numero)
        else:
            resultado -= int(numero)
        respuesta += str(resultado) + ', '
    respuestas.append(respuesta[:len(respuesta) - 1])
for respuesta in respuestas:
    print(respuesta)

