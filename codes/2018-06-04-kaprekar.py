from functools import reduce

if __name__ == '__main__':
    soluciones = []
    número_casos = int(input())
    for _ in range(número_casos):
        número = input()
        solución = -1
        if número == '6174':
            solución = 0
        elif reduce(lambda x, y: x and y, list(map(lambda x: número[0] == x, número))):
            solución = 8
        else:
            pass
        soluciones.append(solución)
    for solución in soluciones:
        print(solución)
