if __name__ == '__main__':
    respuestas = []
    numeros_potitos = int(input())
    while numeros_potitos != 0:
        set_si = set()
        set_no = set()
        for i in range(numeros_potitos):
            posicion = 1
            potito = input().split(' ')
            if potito[0] == 'SI:':
                while potito[posicion] != 'FIN':
                    set_si.add(potito[posicion])
                    posicion += 1
            else:
                while potito[posicion] != 'FIN':
                    set_no.add(potito[posicion])
                    posicion += 1

        ingredientes = list(set_no - set_si)
        sorted(ingredientes)
        respuesta = ''
        for ingrediente in ingredientes:
            respuesta += ingrediente + ' '
        respuestas.append(respuesta)
        numeros_potitos = int(input())
    for respuesta in respuestas:
        print(respuesta)
