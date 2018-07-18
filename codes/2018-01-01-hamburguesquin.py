class Intervalo:

    def __init__(self, centro, radio):
        self.centro = centro
        self.radio = radio

    def extremo_izquierdo(self):
        return self.centro - self.radio

    def extremo_derecho(self):
        return self.centro + self.radio

    def __eq__(self, intervalo):
        return self.centro == intervalo.centro and self.radio == intervalo.radio

    def __ne__(self, intervalo):
        return self.centro != intervalo.centro and self.radio != intervalo.radio

    def __le__(self, intervalo):
        return self.extremo_izquierdo() <= intervalo.extremo_izquierdo()

    def __lt__(self, intervalo):
        return self.extremo_izquierdo() < intervalo.extremo_izquierdo()

    def __ge__(self, intervalo):
        return self.extremo_izquierdo() >= intervalo.extremo_izquierdo()

    def __gt__(self, intervalo):
        return self.extremo_izquierdo() > intervalo.extremo_izquierdo()

    def __str__(self):
        extremo_izquierdo = self.extremo_izquierdo()
        extremo_derecho = self.extremo_derecho()
        return f'[{extremo_izquierdo}, {extremo_derecho}]'

    def __repr__(self):
        return f'{self.__class__.__name__}({self.centro}, {self.radio})'


if __name__ == '__main__':
    soluciones = []
    longitud, restaurantes = [int(x) for x in input().split()]
    while longitud and restaurantes:
        lista_restaurantes = []
        for _ in range(restaurantes):
            centro, radio = [int(x) for x in input().split()]
            lista_restaurantes.append(Intervalo(centro, radio))
        lista_restaurantes.sort()
        if lista_restaurantes[0].extremo_izquierdo() > 1:
            soluciones.append(-1)
        else:
            eliminables = 0
            posición = 1
            while posición < len(lista_restaurantes) and \
                    lista_restaurantes[posición - 1].extremo_derecho() >= lista_restaurantes[posición].extremo_izquierdo():
                if posición < len(lista_restaurantes) - 1 and \
                        lista_restaurantes[posición].extremo_derecho() >= lista_restaurantes[posición + 1].extremo_izquierdo():
                    eliminables += 1
                posición += 1
            if posición == len(lista_restaurantes) and lista_restaurantes[posición - 1].extremo_derecho() >= longitud:
                soluciones.append(eliminables)
            else:
                soluciones.append(-1)
        longitud, restaurantes = [int(x) for x in input().split()]

    for solucion in soluciones:
        print(solucion)
