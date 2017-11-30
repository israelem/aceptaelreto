def genera_numero(lenght):
    res = ''
    for n in range(1, lenght + 1):
        res += str(n)
    return int(res)


if __name__ == "__main__":
    respuestas = []
    iteraciones = int(input())
    for i in range(iteraciones):
        longitud = int(input())
        numero = genera_numero(longitud)
        if numero % 3 == 0:
            respuestas.append('SI')
        else:
            respuestas.append('NO')
    for respuesta in respuestas:
        print(respuesta)
