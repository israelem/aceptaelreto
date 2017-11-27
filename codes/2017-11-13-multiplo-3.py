if __name__ == "__main__":
    respuestas = []
    iteraciones = int(input())
    for i in range(iteraciones):
        numero = int(input())
        if numero % 3 == 0:
            respuestas.append('SI')
        else:
            respuestas.append('NO')
    for respuesta in respuestas:
        print(respuesta)
