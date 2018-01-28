if __name__ == '__main__':
    velocidades = [int(x) for x in input().split(' ')]
    velocidades = velocidades[1:]
    print(max(velocidades))
