if __name__ == '__main__':
    BASE = 6
    casos = int(input())
    respuestas = []
    for i in range(casos):
        numero = int(input())
        numero_base = ''
        while numero != 0:
            numero_base = str(numero % BASE) + numero_base
            numero = numero // BASE
        respuestas.append(numero_base)
    for numero in respuestas:
        print(numero)
