from datetime import time


class Pelicula:
    def __init__(self, inicio: str, duración: str):
        self.inicio = time(hour=int(inicio.split(':')[0]), minute=int(inicio.split(':')[1]))
        self.fin = Pelicula._fin(self.inicio, int(duración))

    @staticmethod
    def _fin(inicio: time, duración: int):
        minutos = inicio.hour*60 + inicio.minute + duración + 10
        return time(hour=(minutos // 60), minute=(minutos % 60))


    def __le__(self, pelicula):
        return self.inicio.hour < pelicula.inicio.hour or (self.inicio.hour == pelicula.inicio.hour and
                                                           self.inicio.minute <= pelicula.inicio.minute)

    def __lt__(self, pelicula):
        return self.inicio.hour < pelicula.inicio.hour or (self.inicio.hour == pelicula.inicio.hour and
                                                           self.inicio.minute < pelicula.inicio.minute)

    def __str__(self):
        return f'{self.inicio.hour}:{self.inicio.minute}, {self.fin.hour}:{self.fin.minute}'

if __name__ == '__main__':
    soluciones = []
    numero_peliculas = int(input())
    while numero_peliculas:
        lista_peliculas = []
        for _ in range(numero_peliculas):
            inicio, duración = input().split()
            lista_peliculas.append(Pelicula(inicio, duración))
        lista_peliculas.sort()
        numero_peliculas = int(input())
