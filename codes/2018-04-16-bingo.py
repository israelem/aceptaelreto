respuestas = []
numero_bolas = int(input())
while numero_bolas:
    bolas = [int(x) for x in input().split()]
    bolas.sort(reverse=True)
    diferencias = set()
    for indice, valor in enumerate(bolas):
        diferencias = diferencias.union(set(map(lambda x: valor - x, bolas[indice + 1:])))
    respuestas.append(sorted(list(diferencias)))
    numero_bolas = int(input())

for respuesta in respuestas:
    for numero in respuesta:
        print(numero, end=' ')
    print()
