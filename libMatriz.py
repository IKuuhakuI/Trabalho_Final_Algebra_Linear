#def criaMatriz(linhas, colunas):
#	mat = ['1'] * linhas
#
#	for i in range(linhas):
#		mat[i] = ['1'] * colunas
#
#	return mat


def MostrarMatriz (matriz):
	for i in range(linhas):
		print(matriz [i])


def GerarMatrizTransposta (matrizOrigem, matrizTransposta):
	linhas = len (matrizOrigem)
	colunas = len (matrizOrigem [0])

	for j in range (colunas):

		linhaAtual = []

		for i in range (linhas):
			linhaAtual.append (matrizOrigem [i][j])

		matrizTransposta.append (list(linhaAtual))
	
def MultiplicarMatrizes (matA, matB, linA, colA, colB):

	resultado = criaMatriz(linA, colB)

	for i in range(linA):
		for k in range(colB):
			soma = 0
			for j in range(colA):
				soma = soma + matA[i][j] * matB[j][k]
			resultado[i][k] = soma

	return resultado
