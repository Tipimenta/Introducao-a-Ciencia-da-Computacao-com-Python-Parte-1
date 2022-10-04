def maior_primo(x):
    j = x
    while j > 1 and eprimo(j) == False:
        j = j - 1
    return j


def eprimo(x):
    i = 1
    contador = 0
    while i <= x:
        if x % i == 0:
            contador = contador + 1
        i = i + 1
    if contador > 2:
        return False
    else:
        return True