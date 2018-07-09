soluciones = []
billetes, participantes = [int(x) for x in input().split()]
while billetes and participantes:
    lista_billetes = [int(x) for x in input().split()]
    reparto = [[] for _ in range(participantes)]
    for posicion, billete in enumerate(lista_billetes):
        reparto[posicion % participantes].append(billete)
    soluciones.append(reparto)
    billetes, participantes = [int(x) for x in input().split()]

for solucion in soluciones:
    for botin in solucion:
        print(sum(botin), ': ', end='')
        for billete in botin:
            print(billete, end=' ')
        print()
    print('---')
