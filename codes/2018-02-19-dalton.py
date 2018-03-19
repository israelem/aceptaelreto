respuestas = []
numero_personas = int(input())
while numero_personas:
    personas = [int(x) for x in input().split()]
    anterior = personas[0]
    dalton = True
    for x in personas[1:]:
        dalton = dalton and anterior < x
        anterior = x
    if dalton:
        respuestas.append('DALTON')
    else:
        respuestas.append('DESCONOCIDOS')
    numero_personas = int(input())
for respuesta in respuestas:
    print(respuesta)
