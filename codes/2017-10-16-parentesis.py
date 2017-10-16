if __name__ == '__main__':
    cadena = input()
    lista_p = []
    respuesta = "YES"
    i = 0
    while respuesta == "YES" and i < len(cadena):
        if c in "{[(":
            lista_p.append(c)
        elif c in "}])" and not len(lista_p) or
            c in "}])" and len(lista_p) and lista_p[len(lista_p) - 1] != c:
            respuesta = "NO"
        elif c in "}])" and len(lista_p) and lista_p[len(lista_p) - 1] == c:
            lista_p = lista_p[ : len(lista_p)]
        i += 1
    print(respuesta)
