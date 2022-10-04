numero = -1
lista = []
while numero != 0:
    numero = int(input("Digite um número: "))
    if numero == 0:
        break
    lista.append(numero)

for i in lista[::-1]:
    print(i)
