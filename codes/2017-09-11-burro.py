if __name__ == '__main__':
    soluciones = []
    numero_casos = int(input())
    for i in range(numero_casos):
        parejas = 0
        burros, sacos = [int(x) for x in input().split(' ')]
        lista_sacos = [int(x) for x in input().split(' ')]
        while lista_sacos:
            peso = lista_sacos[0]
            ocurrencias = lista_sacos.count(peso)
            parejas += ocurrencias // 2
            lista_sacos = [saco for saco in lista_sacos if saco != peso]            
        if parejas < burros:
            soluciones.append(parejas)
        else:
            soluciones.append(burros)
    for solucion in soluciones:
        print(solucion)
