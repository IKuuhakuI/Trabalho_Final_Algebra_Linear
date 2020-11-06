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
	for linha in matrizOrigem:
		if linha [-1] == "Iris-setosa":
			irisSetosa.append (linha[1:-1])

		elif linha [-1] == "Iris-versicolor":
			irisVersicolor.append (linha[1:-1])
	
		else:
			irisVirginica.append (linha[1:-1])


# TESTES ########
#matrizOrigem = []
#
#matriz1 = []
#matriz2 = []
#matriz3 = []
#
#LerCsv ("Iris.csv", matrizOrigem, 1)
#
#SepararTipos (matrizOrigem, matriz1, matriz2, matriz3)
#
#print (matriz1)
#input ()
#print (matriz2)
#input()
#print (matriz3)
