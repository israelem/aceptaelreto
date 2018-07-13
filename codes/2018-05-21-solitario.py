from dataclasses import dataclass, field
from typing import List


# Ejercicio: https://www.aceptaelreto.com/problem/statement.php?id=187

@dataclass
class Carta:
    valor: int
    palo: str

    def siguiente(self, carta):
        # En el caso del 7 la siguiente es la sota
        return self.valor - 1 == carta.valor \
               or (self.valor == 10 and carta.valor == 7)

    def __eq__(self, carta):
        return self.palo == carta.palo and self.valor == carta.valor

    def __ne__(self, carta):
        return self.palo != carta.palo or self.valor != carta.valor

    def __ge__(self, carta):
        return self.palo == carta.palo and self.valor >= carta.valor

    def __gt__(self, carta):
        return self.palo == carta.palo and self.valor > carta.valor

    def __le__(self, carta):
        return self.palo == carta.palo and self.valor <= carta.valor

    def __lt__(self, carta):
        return self.palo == carta.palo and self.valor < carta.valor

    def __str__(self):
        palos = {
            'E': 'espadas',
            'B': 'bastos',
            'O': 'oros',
            'C': 'copas'
        }
        valores = {
            1: 'as',
            10: 'sota',
            11: 'caballo',
            12: 'rey'
        }
        palo = palos[self.palo]
        if self.valor in valores.keys():
            valor = valores.get(self.valor)
        else:
            valor = self.valor
        return f'{valor} de {palo}'


@dataclass
class Mazo:
    mazo: List[Carta] = field(default_factory=list)

    def añadir_carta(self, carta):
        self.mazo.append(carta)

    def coger_última_carta(self):
        return self.mazo.pop()

    def coger_primera_carta(self):
        return self.mazo.pop(0)

    def última_carta(self):
        return self.mazo[len(self.mazo) - 1]

    def vacio(self):
        return len(self.mazo) == 0

    def dar_vuelta(self):
        return Mazo(self.mazo[::-1])

    def __str__(self):
        cadena = 'mazo vacío'
        if len(self.mazo):
            cadena = ''
            for carta in self.mazo:
                cadena += str(carta) + '\n'
        return cadena


def continuar(mazos):
    palos = {
        'E': 'espadas',
        'B': 'bastos',
        'O': 'oros',
        'C': 'copas'
    }
    continuar = False
    for carta in mazos['mano'].mazo:
        continuar = continuar \
                    or (mazos[palos[carta.palo]].vacio() and carta.valor == 1
                        or (not mazos[palos[carta.palo]].vacio()
                            and carta.siguiente(mazos[palos[carta.palo]].última_carta())))
    return continuar


def colocar_cartas(mazos):
    palos = {
        'E': 'espadas',
        'B': 'bastos',
        'O': 'oros',
        'C': 'copas'
    }

    while not mazos['mesa'].vacio() \
            and ((mazos[palos[mazos['mesa'].última_carta().palo]].vacio()
                 and mazos['mesa'].última_carta().valor == 1) \
            or (not mazos[palos[mazos['mesa'].última_carta().palo]].vacio() and
                mazos['mesa'].última_carta().siguiente(mazos[palos[mazos['mesa'].última_carta().palo]].última_carta()))):
        carta = mazos['mesa'].coger_última_carta()
        mazos[palos[carta.palo]].añadir_carta(carta)


if __name__ == '__main__':
    soluciones = []
    numero_palos = int(input())
    while numero_palos:
        mazos = {
            'mano': Mazo(),
            'mesa': Mazo(),
            'bastos': Mazo(),
            'copas': Mazo(),
            'espadas': Mazo(),
            'oros': Mazo()
        }

        lista_cartas = input().split()
        lista_valores = lista_cartas[::2]
        lista_palos = lista_cartas[1::2]
        for valor, palo in zip(lista_valores, lista_palos):
            mazos['mano'].añadir_carta(Carta(int(valor), palo))
        while continuar(mazos):
            while not mazos['mano'].vacio():
                mazos['mesa'].añadir_carta(mazos['mano'].coger_primera_carta())
                if not mazos['mano'].vacio():
                    mazos['mesa'].añadir_carta(mazos['mano'].coger_primera_carta())
                colocar_cartas(mazos)
            mazos['mano'] = mazos['mesa'].dar_vuelta()
            mazos['mesa'] = Mazo()
        if mazos['mano'].vacio():
            soluciones.append('GANA')
        else:
            soluciones.append('PIERDE')
        numero_palos = int(input())
    for solucion in soluciones:
        print(solucion)
