def resolver(inicio, fin, iteraciones, maximo):
    if iteraciones == maximo:
        respuesta = MAX
    elif inicio == fin:
        respuesta = iteraciones
    else:
        inicio_suma = (inicio + 1) % MAX
        inicio_prod = (inicio * 2) % MAX
        inicio_div = (inicio // 3) % MAX
        respuesta = min(resolver(inicio_suma, fin, iteraciones + 1, maximo),
                        resolver(inicio_prod, fin, iteraciones + 1, maximo),
                        resolver(inicio_div, fin, iteraciones + 1, maximo))
    return respuesta

if __name__ == '__main__':
    MAX = 10000
    inicio, fin = [int(x) for x in input().split(' ')]
    if 0 <= inicio < MAX and 0 <= fin < MAX:
        iteraciones = 0
        maximo = 1
        pulsaciones = MAX
        while pulsaciones == MAX and maximo <= MAX:
            pulsaciones = resolver(inicio,fin, iteraciones, maximo)
            maximo += 1
        if pulsaciones < MAX:
            print(pulsaciones)
        else:
            print("NÚMERO FINAL NO ALCANZADO")
    else:
        print("NÚMEROS FUERA DE RANGO")
