from random import randrange
import sudoku_test as sudokuTest

matriz =  [['.', ".", ".", ".", ".", ".", ".", ".", "."],
           [".", ".", ".", ".", ".", ".", ".", ".", "."],
           [".", ".", ".", ".", ".", ".", ".", ".", "."],
           [".", ".", ".", ".", ".", ".", ".", ".", "."],
           [".", ".", ".", ".", ".", ".", ".", ".", "."],
           [".", ".", ".", ".", ".", ".", ".", ".", "."],
           [".", ".", ".", ".", ".", ".", ".", ".", "."],
           [".", ".", ".", ".", ".", ".", ".", ".", "."],
           [".", ".", ".", ".", ".", ".", ".", ".", "."]]


def gerarSudoku():

    qtd = 0

    while (qtd < 30):
        linha = randrange(0, 9)
        coluna = randrange(0, 9)
        valor = randrange(0, 9)
        numeroValido = False

        if matriz[linha][coluna] == '.':
            matriz[linha][coluna] = valor

            teste = sudokuTest.verificarLinha(linha, coluna, matriz)

            if teste is True:
                teste = sudokuTest.verificarColuna(linha, coluna, matriz)

                if teste is True:
                    teste = sudokuTest.verificarBloco(linha, coluna, matriz)

            if teste is False:
                while numeroValido is False:
                    matriz[linha][coluna] = randrange(0, 9)
                    numeroValido = sudokuTest.verificarLinha(linha, coluna, matriz)

                    if numeroValido is True:
                        numeroValido = sudokuTest.verificarColuna(linha, coluna, matriz)

                        if numeroValido is True:
                            numeroValido = sudokuTest.verificarBloco(linha, coluna, matriz)


            qtd = qtd + 1

    return matriz