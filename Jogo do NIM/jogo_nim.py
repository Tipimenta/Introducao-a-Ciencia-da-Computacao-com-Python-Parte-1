def computador_escolhe_jogada(n, m):
    remove = 1
    while remove != m:
        if (n - remove) % (m+1) == 0:
            return remove
        else:
            remove = remove + 1
    return remove

def usuario_escolhe_jogada(n, m):
    print()
    jogada = int(input("Quantas peças você vai tirar? "))
    while jogada < 1 or jogada > m:
        print("Oops! Jogada inválida! Tente de novo.")
        jogada = int(input("Digite quantas peças deseja remover. "))
    return jogada


def partida():
    pecas_validas = False
    while not pecas_validas:
        n = int(input("Quantas peças? "))
        m = int(input("Limite de peças por jogada? "))
        if m > n:
            print("\nOops! Número de peças a retirar inválido! Tente de novo.\n")
        else:
            pecas_validas = True
    vezPC = False
    if n % (m+1) == 0:
        print()
        print("Você começa!")
    else:
        print()
        print("Computador começa!")
        vezPC = True
    while n > 0:
        if vezPC:
            pc = computador_escolhe_jogada(n, m)
            n = n - pc
            print()
            print(f"O computador tirou {pc} peça.")
            print(f"Agora resta apenas {n} no tabuleiro.")
            if n == 0:
                print("Fim do jogo! O computador ganhou!")
                return 2
            vezPC = False
        else:
            usuario = usuario_escolhe_jogada(n, m)
            n = n - usuario
            print()
            print(f"Você tirou {usuario} peça")
            print(f"Agora resta apenas {n} no tabuleiro.")
            if n == 0:
                print('Fim do jogo! Voce ganhou!')
                return 1
            vezPC = True

def campeonato():
    pontuacao = usuario_pontos = computador_pontos = 0
    i = 1
    while i <= 3:
        print()
        print(f"**** Rodada {i} ****\n")
        pontuacao = partida()
        if pontuacao == 1:
            usuario_pontos += 1
        elif pontuacao == 2:
            computador_pontos += 1
        i+= 1

    print("**** Final do campeonato! ****/n")
    print(f"Placar: Você {usuario_pontos} X {computador_pontos} Computador")


def main():
    print("Bem-vindo ao jogo do NIM! Escolha:")
    print("1 - para jogar uma partida isolada")
    print("2 - para jogar um campeonato 2")
    opcao = int(input("opcao: "))

    if opcao == 1:
        print("Voce escolheu uma partida!\n")
        partida()
    elif opcao == 2:
        print("Voce escolheu um campeonato!\n")
        campeonato()
    else:
        print("\nOops! Jogada inválida! Tente de novo.\n")

main()


