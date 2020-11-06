from libFormatar import LerCsv, SepararTipos, FormatarMatriz

# TESTES ########
matrizOrigem = []

matriz1 = []
matriz2 = []
matriz3 = []

LerCsv ("Iris.csv", matrizOrigem, 1)

SepararTipos (matrizOrigem, matriz1, matriz2, matriz3)

matrizIndependente1 = []
matrizDependente1 = []

FormatarMatriz (matriz1, matrizIndependente1, matrizDependente1) 

print ("Matriz 1:")
print (matriz1)
print("\nMatriz 1 formatada: ")
print (matrizIndependente1)
print (matrizDependente1)
print ()
print (matriz2)
print ()
print (matriz3)
