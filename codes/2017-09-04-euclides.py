respuestas = []
casos = int(input())
for i in range(casos):
    dividendo, divisor = [int(x) for x in input().split( ' ')]
    if divisor == 0:
        respuestas.append('DIV0')
    elif dividendo > 0:
        cociente = 0
        resto = dividendo
        abs_divisor = abs(divisor)
        while resto > abs_divisor:
            resto -= abs_divisor
            cociente += 1
        if divisor < 0:
            cociente *= -1
        respuestas.append('%d %d' % (cociente, resto))
    else:
        cociente = 0
        resto = dividendo
        abs_divisor = abs(divisor)
        while abs(resto) > abs_divisor:
            resto += abs_divisor
            cociente += 1
        if divisor > 0:
            cociente *= -1
        respuestas.append('%d %d' % (cociente, resto))
for respuesta in respuestas:
    print(respuesta)
