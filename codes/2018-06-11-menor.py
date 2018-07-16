def suma_cifras(número):
    return sum([int(c) for c in str(número)])


if __name__ == '__main__':
    soluciones = []
    menor = int(input())
    while menor:
        prueba = 1
        suma = suma_cifras(prueba)
        while menor != suma:
            prueba += 1
            suma = suma_cifras(prueba)
        soluciones.append(prueba)
        menor = int(input())
    for solucion in soluciones:
        print(solucion)
