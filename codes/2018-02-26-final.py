from functools import reduce

if __name__ == '__main__':
    numero = int(reduce(lambda x, y: x + y, [x for x in input().split('.')])) + 1
    cadena = ''
    for x in range(len(str(numero)) - 1, -1, -3):
        if x - 3 >= 0:
            cadena += str(numero)[x:x - 3:-1] + '.'
        else:
            cadena += str(numero)[x::-1]
    print(cadena[::-1])
