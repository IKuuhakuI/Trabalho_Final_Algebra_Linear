from libMatriz import MostrarMatriz, GeraMatrizTransposta, MultiplicarMatrizes

print("\nI - GERANDO MATRIZES DE TESTE\n")

matriz5x1 = [0] * 5
for linha in range(5):
    matriz5x1[linha] = linha
print("Matriz 5x1: ")
print(matriz5x1)

matriz5x5 = [0] * 5
for linha in range(5):
    matriz5x5[linha] = [linha, linha+1, linha+2, linha+3, linha+4]
print("Matriz 5x5: ")
print(matriz5x5)

print("\nI - TESTE MOSTRAR MATRIZ \n")

MostrarMatriz(matriz5x1)
MostrarMatriz(matriz5x5)

print("\nII - TESTE GERAR MATRIZ TRANSPOSTA \n")

matriz5x1Transposta = []
matriz5x5Transposta = []
GeraMatrizTransposta(matriz5x1, matriz5x1Transposta)
GeraMatrizTransposta(matriz5x5, matriz5x5Transposta)
MostrarMatriz(matriz5x1Transposta)
MostrarMatriz(matriz5x5Transposta)

print("\nIII - TESTE MULTIPLICAR MATRIZES \n")

matriz5x1VezesTransposta = []
matriz5x5VezesTransposta = []
MultiplicarMatrizes(matriz5x1, matriz5x1Transposta, matriz5x1VezesTransposta)
MultiplicarMatrizes(matriz5x5, matriz5x5Transposta, matriz5x5VezesTransposta)
MostrarMatriz(matriz5x1VezesTransposta)
MostrarMatriz(matriz5x5VezesTransposta)

print()


# def GerarMatrizTeste(numeroLinhas, numeroColunas):
#    matriz = [0] * numeroLinhas
#    for linha in range(numeroLinhas):
#        matriz[linha] = [0] * numeroColunas
#    return matriz


#matrizLinha = GerarMatrizTeste(15, 1)
#print ("Matriz Linha:")
# print(matrizLinha)

#matriz1x15 = criaMatriz(1, 15)
# print(matriz1x15)
#matriz15x1 = criaMatriz(15, 1)
# print(matriz15x1)

#resultado = geraMatrizResultado(1, 15)

#print("Nosso Resultado: ")
#mostraMatriz(resultado, 15)
# print("\n")
#print("Nossa Matriz: ")
#mostraMatriz(matriz, 4)
