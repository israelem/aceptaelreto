if __name__ == '__main__':
    # Leer número equipos y globos
    equipos, globos = [int(x) for x in list(input().split(' '))]
    while equipos != 0 and globos != 0 and 1 <= equipos <= 20:
        # Generar el diccionario para las puntuaciones
        # se utiliza diccionario porque el equipo más bajo es el 1
        # Además, al ser un diccionario no podemos aprovechar las
        # listas por comprensión
        puntuaciones_equipos = {}
        for x in range(1, equipos+1):
            puntuaciones_equipos[x] = 0
        # Se leen los globos ganados por cada equipo
        # no nos importa el color, por eso no se utiliza
        for x in range(globos):
            equipo, color = [x for x in list(input().split(' '))]
            equipo = int(equipo)
            puntuaciones_equipos[equipo] += 1
        # Se busca el más alto o máximo
        # Si dos equipos tienen la misma puntuación, entonces hay empate
        # Si otro equipo tiene más puntuación, rompe el empate
        equipo_ganador = 0
        empate = False
        for equipo in puntuaciones_equipos.keys():
            if puntuaciones_equipos[equipo] > puntuaciones_equipos[equipo_ganador]:
                equipo_ganador = equipo
                empate = False
            elif puntuaciones_equipos[equipo] == puntuaciones_equipos[equipo_ganador]:
                empate = True
        if empate:
            print("EMPATE")
        else:
            print(equipo_ganador)
        equipos, globos = [int(x) for x in list(input().split(' '))]
