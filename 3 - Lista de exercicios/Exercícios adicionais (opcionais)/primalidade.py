n = int(input("Digite um número inteiro: "))

i = 1
contador = 0
while i <= n:
        if n % i == 0:
            contador = contador + 1
        i = i + 1
        print (contador)
if contador == 2:
    print("primo")
else:
    print("não primo")