if __name__ == '__main__':
    paises = int(input())
    respuestas = []
    while paises != 0:
        estudiantes = [int(x) for x in list(input().split(' '))]
        if paises == len(estudiantes):
            parejas = 0
            for posicion in range(len(estudiantes)):
                parejas += (estudiantes[posicion]*(sum(estudiantes[posicion+1:len(estudiantes)])))
            respuestas.append(parejas)
        else:
            respuestas.append("El número de países escritos no coincide con los indicados")
        paises = int(input())
    for x in respuestas:
        print(x)
