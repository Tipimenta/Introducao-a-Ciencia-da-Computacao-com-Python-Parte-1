linha = int(input("Digite a largura: "))
coluna = int(input("Digite a altura: "))

# zerando as variaveis
l = 0
c = 0

# enquanto c menor que o numero de colunas digitados
while c  < coluna:
    # enquanto l menor que o numero de linhas digitados
    while l  < linha:
        # printa o conteudo # sem pular para a proxima linha devido ao end = ""
        print("#", end = "")
        # adiciona mais 1 ao l, para continuar printando a quantidade de linhas
        l =  l  + 1
    # pula uma linha apos o fim da linha
    print()
    # adiciona mais 1 ao c indicando a proxima coluna
    c = c  + 1
    # zera novamente as linhas para imprimir a partir do inicio até a quantidade digitada
    l = 0