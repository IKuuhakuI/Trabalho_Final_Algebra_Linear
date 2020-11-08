#def criaMatriz(linhas, colunas):
#	mat = ['1'] * linhas
#
#	for i in range(linhas):
#		mat[i] = ['1'] * colunas
#
#	return mat


def MostrarMatriz (matriz):

	linhas = len (matriz)
	colunas = len (matriz [0])

	print (end="\t")

	for contador in range (colunas):
		print ("----------------", end="")
	print ()

	for i in range (linhas):

		print ("\t|\t", end="")

		for j in range (colunas):
			
			temp = float ("{:.2f}".format(matriz[i][j]))

			print(temp, end = "\t")

			if j < (colunas - 1):
				print ("|", end="\t")			
			else:
				print ("|", end="")

		print ("\n", end="\t")

		for contador in range (colunas):
			print ("----------------", end="")

		print ()

def GerarMatrizTransposta (matrizOrigem, matrizTransposta):
	linhas = len (matrizOrigem)
	colunas = len (matrizOrigem [0])

	for j in range (colunas):

		linhaAtual = []

		for i in range (linhas):
			linhaAtual.append (matrizOrigem [i][j])

		matrizTransposta.append (list(linhaAtual))
	
def MultiplicarMatrizes (primeiraMatriz, segundaMatriz, matrizResultado):

	linhasPrimeiraMatriz = len (primeiraMatriz)
	colunasPrimeiraMatriz = len (primeiraMatriz [0])

	linhasSegundaMatriz = len (segundaMatriz)
	colunasSegundaMatriz = len (segundaMatriz [0])

	for i in range (linhasPrimeiraMatriz):
		linhaAtual = []

		for j in range (colunasSegundaMatriz):
			valorAtual = 0

			for indice in range (colunasPrimeiraMatriz):	
				valorAtual += primeiraMatriz [i][indice] * segundaMatriz [indice][j]

			linhaAtual.append (valorAtual)

		matrizResultado.append (list (linhaAtual))
