def es_primo(numero):
    if numero <= 1:
        return False
    elif numero <= 3:
        return True
    elif numero % 2 == 0 or numero % 3 == 0:
        return False
    i = 5
    while i * i <= numero:
        if numero % i == 0 or numero % (i + 2) == 0:
            return False
        i += 6
    return True

def encontrar_primos(inicio, fin):
    primos = []
    for num in range(inicio, fin + 1):
        if es_primo(num):
            primos.append(num)
    return primos

def guardar_resultados(primos):
    with open('results.txt', 'w') as archivo:
        for primo in primos:
            archivo.write(str(primo) + '\n')

if __name__ == '__main__':
    primos = encontrar_primos(1, 250)
    guardar_resultados(primos)
    print("Los números primos entre 1 y 250 se han guardado en results.txt")