def suma_n_numeros(n):
    return (pow(n,2)+n)/2

if __name__ == '__main__':
    numero_piedras = int(input())
    while(numero_piedras > 0):
        i = 1;
        while(suma_n_numeros(i)<numero_piedras):
            i += 1
        i -= 1
        sobran = numero_piedras - suma_n_numeros(i)
        print(str(i) + " " + str(int(sobran)))
        numero_piedras = int(input())
