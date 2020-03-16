def verificarLinha(linha, coluna, matriz):
    num = matriz[linha][coluna]
    qtd = 0

    for y in range(0, len(matriz)):
        cont = y
        if matriz[linha][y] == num:
            qtd = qtd + 1

            if qtd > 1:
                return False

        if cont == 8 and qtd < 2:
            return True


def verificarColuna(linha, coluna, matriz):
    num = matriz[linha][coluna]
    qtd = 0

    for x in range(0, len(matriz)):
        cont = x
        if matriz[x][coluna] == num:
            qtd = qtd + 1

            if qtd > 1:
                return False

        if cont == 8 and qtd < 2:
            return True


def verificarBloco(linha, coluna, matriz):
    num = matriz[linha][coluna]
    qtd = 0
    bloco = []

    # Bloco01
    if linha <= 2 and coluna <= 2:
        bloco = [0, 0]

    # Bloco02
    elif linha <= 2 and (2 < coluna <= 5):
        bloco = [0, 3]

    # Bloco03
    elif linha <= 2 and (5 < coluna <= 8):
        bloco = [0, 6]

    # Bloco04
    elif (2 < linha <= 5) and (coluna <= 2):
        bloco = [3, 0]

    # Bloco05
    elif (2 < linha <= 5) and (2 < coluna <= 5):
        bloco = [3, 3]

    # Bloco06
    elif (2 < linha <= 5) and (5 < coluna <= 8):
        bloco = [3, 6]

    # Bloco07
    elif (5 < linha <= 8) and (coluna <= 2):
        bloco = [6, 0]

    # Bloco08
    elif (5 < linha <= 8) and (2 < coluna <= 5):
        bloco = [6, 3]

    # Bloco09
    elif (5 < linha <= 8) and (5 < coluna <= 8):
        bloco = [6, 6]


    bx = bloco[0]
    by = bloco[1]
    tamX = bloco[0] + 3
    tamY = bloco[1] + 3
    cont = 0


    for x in range(bx, tamX):
        for y in range(by, tamY):
            cont = cont+1
            if matriz[x][y] == num:
                qtd = qtd + 1
                if qtd > 1:
                    return False

            if cont == 9 and qtd < 2:
                return True


def testarSudoku(linha, coluna, matriz):

    resultado = verificarLinha(linha, coluna, matriz)

    if resultado is True:
        resultado = verificarColuna(linha, coluna, matriz)

        if resultado is True:
            resultado = verificarBloco(linha, coluna, matriz)

    return resultado