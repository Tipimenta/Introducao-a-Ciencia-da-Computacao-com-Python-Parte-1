n = int(input("Digite um número inteiro: "))

i = 0
atual = 0
anterior = 0
pesquisa = 0
while i <=n :
    atual = n % 10
    n = n // 10
    anterior = n % 10
    i = i + 1
    if atual == anterior and n != 0:
        pesquisa = 1
if pesquisa == 1:
    print("sim")
else:
    print("não")
