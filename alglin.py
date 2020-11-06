import csv
from libMatriz import geraMatriz, geraMatrizResultado, mostraMatriz

matriz = geraMatriz(1, 15)
resultado = geraMatrizResultado(1, 15)

print("Nosso Resultado: ")
mostraMatriz(resultado, 15)
print("\n")
print("Nossa Matriz: ")
mostraMatriz(matriz, 4)
