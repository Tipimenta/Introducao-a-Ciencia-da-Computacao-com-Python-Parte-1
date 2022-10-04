def é_hipotenusa(a, b):
    hipotenusa = a**2 + b**2
    return hipotenusa

def soma_hipotenusas(n):
    h = 1
    soma = 0

    while h <= n:
        h2 = h**2
        a = 1
        sair = True
        while a < n and sair == True:
            b = a
            while b < n and sair == True:
                if h2 == é_hipotenusa(a, b):
                    soma = soma + h
                    sair = False
                b += 1
            a += 1
        h += 1
    return soma 