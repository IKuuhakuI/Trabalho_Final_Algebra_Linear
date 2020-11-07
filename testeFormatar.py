from libFormatar import LerCsv, SepararTipos, FormatarMatriz
from libMatriz import GerarMatrizTransposta, MultiplicarMatrizes

# TESTES ########
matrizOrigem = []

matriz1 = []
matriz2 = []
matriz3 = []

LerCsv ("Iris.csv", matrizOrigem, 1)

SepararTipos (matrizOrigem, matriz1, matriz2, matriz3)

matrizIndependente1 = []
matrizDependente1 = []
matrizTransposta1 = []

FormatarMatriz (matriz1, matrizIndependente1, matrizDependente1) 
GerarMatrizTransposta (matriz1, matrizTransposta1)

print ("Matriz 1:")
print (matriz1)

print ("\nMatriz 1 formatada: ")
print (matrizIndependente1)
print (matrizDependente1)

print ("\nMatriz 1 transposta: ")
print (matrizTransposta1)

print("\n\nTeste de multiplicacao:")
matrizA = [[1, 0, 3], [-2, 1, 2]]
matrizB = [[1, 0], [-1, -2], [0, -3]]
matrizResultado = []

MultiplicarMatrizes (matrizA, matrizB, matrizResultado)
print (matrizA)
print (matrizB)
print (matrizResultado)
