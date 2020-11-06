import csv

def LerCsv (nomeArquivo, matrizOrigem, numeroGrupo):

	with open (nomeArquivo) as irisCsv:
		leitor = csv.reader (irisCsv, delimiter=',');

		linhas = list (leitor)

		for indice in range ((2 * numeroGrupo - 1), (2 * numeroGrupo + 13 + 1)):
			matrizOrigem.append (linhas[indice]);

		for indice in range ((2 * numeroGrupo + 49), (2 * numeroGrupo + 63 + 1)):
			matrizOrigem.append (linhas[indice]);

		for indice in range ((2 * numeroGrupo + 99), (2 * numeroGrupo + 113 + 1)):
			matrizOrigem.append (linhas[indice]);

def SepararTipos (matrizOrigem, irisSetosa, irisVersicolor, irisVirginica):
	for linhaOrigem in matrizOrigem:

		if linhaOrigem [-1] == "Iris-setosa":

			linhaOrigem [-1] = 1

			for indice in range (1, 5):
				linhaOrigem [indice] = float (linhaOrigem [indice])

			irisSetosa.append (linhaOrigem [1:])

		elif linhaOrigem [-1] == "Iris-versicolor":

			linhaOrigem [-1] = 1

			for indice in range (1, 5):
				linhaOrigem [indice] = float (linhaOrigem [indice])

			irisVersicolor.append (linhaOrigem [1:])
	
		else:
			linhaOrigem [-1] = 1

			for indice in range (1, 5):
				linhaOrigem [indice] = float (linhaOrigem [indice])
				
			irisVirginica.append (linhaOrigem [1:])


