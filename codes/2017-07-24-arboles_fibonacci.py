class ArbolBinario:

    def __init__(self, valor, izquierda=None, derecha=None):
        self.__valor = valor
        self.__izquierda = izquierda
        self.__derecha = derecha

    def insertar_izquierda(self, valor):
        self.__izquierda = ArbolBinario(valor)
        return self.__izquierda

    def insertar_derecha(self, valor):
        self.__derecha = ArbolBinario(valor)
        return self.__derecha

    def devolver_valor(self):
        return self.__valor

    def imprimir(self, nivel=0):
        espacios = nivel * '   '
        print('%s%d' % (espacios, self.__valor))
        if self.__izquierda:
            self.__izquierda.imprimir(nivel + 1)
        if self.__derecha:
            self.__derecha.imprimir(nivel + 1)
        return None

def fibonacci(termino):
    if termino == 0:
        return termino
    elif termino == 1:
        return termino
    else:
        return fibonacci(termino - 2) + fibonacci(termino - 1)


def arbol_fibonacci(termino):
    if termino == 0:
        return ArbolBinario(termino)
    elif termino == 1:
        return ArbolBinario(termino)
    else:
        izquierda = arbol_fibonacci(termino - 2)
        derecha = arbol_fibonacci(termino - 1)
        valor = izquierda.devolver_valor() + derecha.devolver_valor()
        arbol = ArbolBinario(valor, izquierda, derecha)
        return arbol


if __name__ == '__main__':
    n = int(input())
    while n >= 0:
        arbol = arbol_fibonacci(n)
        arbol.imprimir()
        print('====')
        n = int(input())
