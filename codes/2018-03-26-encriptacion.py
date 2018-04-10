if __name__ == '__main__':
    fin = False
    respuestas = []
    while not fin:
        mensaje = input()
        desplazamiento = -(ord(mensaje[0]) - ord('p'))
        vocales = 0
        mensaje_decodificado = ''
        for c in mensaje[1:]:
            if ord('A') <= ord(c) <= ord('Z') or ord('a') <= ord(c) <= ord('z'):
                caracter_decodificado = chr(ord(c) + desplazamiento)
                if caracter_decodificado in 'aeiouAEIOU':
                    vocales += 1
            else:
                caracter_decodificado = c
            mensaje_decodificado += caracter_decodificado
        fin = mensaje_decodificado == 'FIN'
        respuestas.append(vocales)
    for respuesta in respuestas[:len(respuestas)-1]:
        print(respuesta)
