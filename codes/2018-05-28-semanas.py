if __name__ == '__main__':
    soluciones = []
    numero_casos = int(input())
    for _ in range(numero_casos):
        días_año, días_semana, día_inicio = [int(x) for x in input().split()]
        días_año -= (días_semana - día_inicio + 1)
        semanas_completas = días_año // días_semana
        soluciones.append(semanas_completas)
    for solucion in soluciones:
        print(solucion)
