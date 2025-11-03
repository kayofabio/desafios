import random

def criar_tabuleiro(linhas, colunas, qtd_minas):
    tabuleiro = []
    minas_locais = []
    minas_colocadas = 0
    for i in range(linhas):
        linha = []
        for j in range(colunas):
            if i == 2 and j == 2:
                linha.append(0)
                continue
            linha.append("~")
            if random.randint(0, 1) > 0 and minas_colocadas <= qtd_minas:
                minas_locais.append([i, j])
                minas_colocadas += 1
        tabuleiro.append(linha)
    return tabuleiro, minas_locais

def mostrar_tabuleiro(tabuleiro):
    for linha in tabuleiro:
        for index, coluna in enumerate(linha):
            print(f"{coluna}  ", end=" ")
            if index == len(tabuleiro)-1:
                print("")

def contar_minas_vizinhas(linha, coluna, minas_locais):
    qtd_minas_vizinhas = 0
    casas_vizinhas = [[linha-1, coluna-1], [linha-1, coluna], [linha-1, coluna+1], [linha, coluna-1], [linha, coluna+1],[linha+1, coluna-1], [linha+1, coluna], [linha+1, coluna+1]]
    for casa in casas_vizinhas:
        if casa in minas_locais:
            qtd_minas_vizinhas += 1
    return qtd_minas_vizinhas

def atualizar_mapa(tabuleiro, marcador, linha, coluna):
    tabuleiro[linha][coluna] = marcador

def jogar(tabuleiro, minas_locais):
    casas_seguras = len(tabuleiro)*len(tabuleiro[0]) - len(minas_locais)
    casas_seguras_descobertas = 1
    casas_jogadas = [[2, 2]]
    print(casas_seguras, casas_seguras_descobertas)
    print("=== CAMPO MINADO ===")
    minas_vizinhas = contar_minas_vizinhas(2, 2, minas_locais)
    # print('gabarito de casas com mina:')
    # for i in minas_locais:
    #     print(i)
    print(f"Há {minas_vizinhas} mina(s) por perto! (2, 2)")
    atualizar_mapa(tabuleiro, minas_vizinhas, 2, 2)
    while True:
        print(f"\ncasas descobertas: {casas_seguras_descobertas}")
        print(f"casas para descobrir: {casas_seguras}")
        print(f"Total de minas: {len(minas_locais)}")
        print("=== tabuleiro ===\n")
        mostrar_tabuleiro(tabuleiro)
        linha_input = input("digite uma linha (0-4): ")
        coluna_input = input("digite uma coluna (0-4): ")
        try:
            linha_input = int(linha_input)
            coluna_input = int(coluna_input)
            if linha_input not in range(len(tabuleiro)) or coluna_input not in range(len(tabuleiro)):
                raise ValueError
        except ValueError:
            print("Valores inválidos! Tente novamente.")
            continue
        if [linha_input, coluna_input] in casas_jogadas:
            print("Esta casa já foi descoberta! tente novamente.")
            continue
        if [linha_input, coluna_input] in minas_locais:
            print("Você explodiu em uma mina!")
            atualizar_mapa(tabuleiro, "X", linha_input, coluna_input)
            mostrar_tabuleiro(tabuleiro)
            print("Game Over!")
            break
        minas_vizinhas = contar_minas_vizinhas(linha_input, coluna_input, minas_locais)
        print(f"Há {minas_vizinhas} mina(s) por perto! ({linha_input}, {coluna_input})")
        atualizar_mapa(tabuleiro, minas_vizinhas, linha_input, coluna_input)
        casas_seguras_descobertas += 1
        casas_jogadas.append([linha_input, coluna_input])
        if casas_seguras_descobertas >= casas_seguras:
            print("PARABÉNS! Você descobriu todas casas sem minas!")
            mostrar_tabuleiro(tabuleiro)
            break
tabuleiro, minas_locais = criar_tabuleiro(5, 5, 10)
jogar(tabuleiro, minas_locais)