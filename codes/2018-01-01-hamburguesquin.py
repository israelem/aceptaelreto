class Intervalo:

    def __init__(self, centro, radio):
        self.centro = centro
        self.radio = radio


if __name__ == '__main__':
    longitud, restaurantes = [int(x) for x in input().split()]
    while longitud and restaurantes:
        lista_restaurantes = []
        for _ in range(restaurantes):
            centro, radio = [int(x) for x in input().split()]
            lista_restaurantes.append(Intervalo(centro, radio))
