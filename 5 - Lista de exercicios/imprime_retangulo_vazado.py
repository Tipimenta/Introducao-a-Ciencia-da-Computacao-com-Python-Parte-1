linha = int(input("Digite o tamanho da linha do retângulo: "))
coluna = int(input("Digite o tamanho da coluna do retângulo: "))

i = 0
while i < coluna:
    j = 0
    while j < linha:
        if i == 0 or i == coluna-1 or j == 0 or j == linha-1:
            print("#"  ,end = "")
        else:
            print(" ",end = "")
        j = j + 1
    print()
    i = i + 1