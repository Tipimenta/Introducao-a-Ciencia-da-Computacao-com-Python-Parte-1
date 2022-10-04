def n_primos(x):

    contador = 0
    i = 1
    j = 2
    primos = 0

    while j <= x:
        i = 1
        contador = 0
        while i <= j:
            if j % i == 0:
                contador = contador + 1
                i = i + 1
            else:
                i = i + 1
        if contador == 2:
            if i >= 2 or i <= x:
                primos = primos + 1
                contador = 0

        j = j + 1
    return primos