from libFormatar import LerCsv, SepararTipos

# TESTES ########
matrizOrigem = []

matriz1 = []
matriz2 = []
matriz3 = []

LerCsv ("Iris.csv", matrizOrigem, 1)

SepararTipos (matrizOrigem, matriz1, matriz2, matriz3)

print (matriz1)
print ()
print (matriz2)
print ()
print (matriz3)
