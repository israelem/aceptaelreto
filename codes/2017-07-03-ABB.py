class ArbolBinarioBusqueda:

    def __init__(self, valor, padre=None, izquierda=None, derecha=None):
        self.valor = valor
        self.padre = padre
        self.izquierda = izquierda
        self.derecha = derecha

    def insertar_izquierda(self, valor):
        añadir = self.valor > valor
        if añadir:
            self.izquierda = ArbolBinarioBusqueda(valor, padre=self)

        return self.izquierda

    def insertar_derecha(self, valor):
        añadir = self.valor < valor
        if añadir:
            self.derecha = ArbolBinarioBusqueda(valor, padre=self)

        return self.derecha

    def devolver_padre(self):
        return self.padre


if __name__ == '__main__':
    IZQ = 'IZQUIERDA'
    DER = 'DERECHA'
    lista_respuestas = []
    numero_casos = int(input())
    for i in range(numero_casos):
        lista_nodos = [int(x) for x in list(input().split(' '))]
        es_bin_busqueda = True
        if lista_nodos[0] != -1:  # Árbol no vacío
            arbol = ArbolBinarioBusqueda(lista_nodos[0])
            nodo_actual = arbol
            rama = IZQ
            posicion_nodo = 1
            es_bin_busqueda = True
            while es_bin_busqueda and posicion_nodo < len(lista_nodos):
                if lista_nodos[posicion_nodo] != -1 and rama == IZQ:
                    nodo_actual = nodo_actual.insertar_izquierda(lista_nodos[posicion_nodo])
                    es_bin_busqueda = nodo_actual is not None
                elif lista_nodos[posicion_nodo] != -1 and rama == DER:
                    nodo_actual = nodo_actual.insertar_derecha(lista_nodos[posicion_nodo])
                    rama = IZQ
                    es_bin_busqueda = nodo_actual is not None
                elif lista_nodos[posicion_nodo] == -1 and rama == IZQ:
                    rama = DER
                elif lista_nodos[posicion_nodo] == -1 and rama == DER:
                    nodo_actual = nodo_actual.devolver_padre()

                posicion_nodo += 1
        if es_bin_busqueda:
            lista_respuestas.append('SI')
        else:
            lista_respuestas.append('NO')
    for respuesta in lista_respuestas:
        print(respuesta)
