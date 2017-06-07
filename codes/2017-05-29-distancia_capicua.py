def capicua(numero):
    return  numero == numero[::-1]

if  __name__ == '__main__':
    inicio = int(input())
    numero = inicio + 1
    while not capicua(str(numero)):
        numero += 1
    print(numero - inicio)


