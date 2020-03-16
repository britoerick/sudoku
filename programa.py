import sudoku as sudoku


matriz = [["5", "3", ".", ".", "7", ".", ".", ".", "."],
          ["6", ".", ".", "1", "9", "5", ".", ".", "."],
          [".", "9", "8", ".", ".", ".", ".", "6", "."],
          ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
          ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
          ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
          [".", "6", ".", ".", ".", ".", "2", "8", "."],
          [".", ".", ".", "4", "1", "9", ".", ".", "5"],
          [".", ".", ".", ".", "8", ".", ".", "7", "9"]]

print("# Matriz informada")
sudoku.imprimirSudoku(matriz)
sudoku.testandoMatriz(matriz)

print("\n\n# Matriz gerada")
matrizGerada = sudoku.gerarSudoku()
sudoku.imprimirSudoku(matrizGerada)
sudoku.testandoMatriz(matrizGerada)