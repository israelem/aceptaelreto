# Comprobar sudoku leído desde teclado
def f_leer_sudoku():
    r_sudoku = []
    # f = open("sudoku.txt", "r")
    for iteracion in range(9):
        # l_str = f.readline().split(' ')
        l_str = str(input()).split(' ')
        r_sudoku.append([int(x) for x in l_str])
    # f.close()
    return r_sudoku


def f_comprobar_linea(p_linea):
    return list(range(1, 10)) == sorted(p_linea)

if __name__ == '__main__':
    correcto = True
    columnas = [[] for i in range(9)]
    cuadrantes = [[] for i in range(9)]
    posicion_fila = 0
    veces = int(input())
    for vez in range(veces):
        sudoku = f_leer_sudoku()
        for fila in sudoku:
            correcto = correcto and f_comprobar_linea(fila)
            posicion_columna = 0
            for casilla in fila:
                columnas[posicion_columna].append(casilla)
                posicion_cuadrante = (posicion_fila // 3) * 3 + (posicion_columna // 3)
                cuadrantes[posicion_cuadrante].append(casilla)
                posicion_columna += 1
            posicion_fila += 1
        for fila in columnas:
            correcto = correcto and f_comprobar_linea(fila)
        for fila in cuadrantes:
            correcto = correcto and f_comprobar_linea(fila)
        if correcto:
            print("SI")
        else:
            print("NO")
