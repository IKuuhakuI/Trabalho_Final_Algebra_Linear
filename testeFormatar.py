from libFormatar import LerCsv, SepararTipos, FormatarMatriz
from libMatriz import MostrarMatriz

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

print ("Matriz 1:")
MostrarMatriz (matriz1)

print ("\nMatriz 1 formatada: ")
MostrarMatriz (matrizIndependente1)
print ()
MostrarMatriz (matrizDependente1)
