if __name__ == '__main__':
    numero_casos = int(input())
    respuestas = []
    for _ in range(numero_casos):
        kilometros = [int(x) for x in input().split()]
        total = 0
        for indice in range(len(kilometros)-1):
            total += sum(kilometros[:indice+1])*2
        respuestas.append(total)
    for respuesta in respuestas:
        print(respuesta)
