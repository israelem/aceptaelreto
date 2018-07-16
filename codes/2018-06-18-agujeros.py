if __name__ == '__main__':
    numero_agujeros, longitud = [int(x) for x in input().split()]
    parches = 1
    agujeros = [int(x) for x in input().split()]
    inicio = agujeros[0]
    for agujero in agujeros[1:]:
        if agujero - inicio > longitud:
            inicio = agujero
            parches += 1
    print(parches)
