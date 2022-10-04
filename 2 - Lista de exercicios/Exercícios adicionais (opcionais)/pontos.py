import math

x1 = int(input("Digite o primeiro numero: "))
y1 = int(input("Digite o segundo numero: "))
x2 = int(input("Digite o terceiro numero: "))
y2 = int(input("Digite o terceiro numero: "))

distancia = ((x1-x2)**2 + (y1-y2)**2)
distancia = math.sqrt(distancia)

if distancia >= 10:
    print("longe")
else:
    print("perto")