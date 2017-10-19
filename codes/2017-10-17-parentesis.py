if __name__ == '__main__':
    cadena = [x for x in input() if x in "{}[]()"]
    if len(cadena) % 2 != 0 or len(cadena) == 0:
        respuesta = "NO"
    else:
        respuesta = "YES"
        i = 0
        while i < len(cadena) and respuesta == "YES":
            if cadena[i] in "{[(":
                i += 1
            else:
                if cadena[i - 1] + cadena[i] in "{}" or \
                        cadena[i - 1] + cadena[i] in "[]" or \
                        cadena[i - 1] + cadena[i] in "()":
                    cadena = cadena[:i - 1] + cadena[i + 1:]
                    i -= 1
                else:
                    respuesta = "NO"
    print(respuesta)
