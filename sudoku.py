import sudoku_test as sudokuTest
from sudoku_generate import gerarSudoku


def testandoMatriz(matriz):
    print("\n********** Testando Matriz Sudoku Informada **********\n")

    resultado = True
    resultado2 = True

    for x in range(0, len(matriz)):
        for y in range(0, len(matriz)):
            if matriz[x][y] != '.':
                resultado = sudokuTest.testarSudoku(x, y, matriz)

                if resultado is False:
                    resultado2 = False

    if resultado is True and resultado2 is True:
        print("Matriz Sudoku é válida")
    else:
        print("Matriz Sudoku Não é Válida")


def imprimirSudoku(matriz):
    print("\n********** Imprimindo Matriz Sudoku Informada **********\n")

    for i in range(0, len(matriz)):
        print(matriz[i])



def gerarMatriz():
    matriz = gerarSudoku()
    return matriz