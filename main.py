from libFormatar import LerCsv, SepararTipos, FormatarMatriz
from libMatriz import GerarMatrizTransposta, MultiplicarMatrizes, MostrarMatriz
from libMenu import MostrarMenu

def main ():
	# Controles do Menu
	criarModeloLinear = True
	opcaoSelecionada = '0'

	# Informacoes para leitura do arquivo CSV
	linhasArquivo = []
	nomeArquivo = "Iris.csv"
	grupo = 1

	# Matrizes com os dados de cada flor
	matrizDadoIrisSetosa = []
	matrizDadoIrisVersicolor = []
	matrizDadoIrisVirginica = []
	
	# Matrizes de cada flor (termo dependente e independente)
	#Iris-setosa
	matrizIrisSetosaDependente = []
	matrizIrisSetosaIndependente = []
	#Iris-versicolor
	matrizIrisVersicolorDependente = []
	matrizIrisVersicolorIndependente = []
	#Iris-virginica
	matrizIrisVirginicaDependente = []
	matrizIrisVirginicaIndependente = []

	# Leitura do arquivo CSV
	LerCsv (nomeArquivo, linhasArquivo, grupo)
	
	# Separando os dados por tipo de flor
	SepararTipos (linhasArquivo, matrizDadoIrisSetosa, matrizDadoIrisVersicolor, matrizDadoIrisVirginica)

	# Formatando os dados
	# Iris-setosa
	FormatarMatriz (matrizDadoIrisSetosa, matrizIrisSetosaIndependente, matrizIrisSetosaDependente)
	# Iris-versicolor
	FormatarMatriz (matrizDadoIrisVersicolor, matrizIrisVersicolorIndependente, matrizIrisVersicolorDependente)
	# Iris-setosa
	FormatarMatriz (matrizDadoIrisVirginica, matrizIrisVirginicaIndependente, matrizIrisVirginicaDependente)
	
	while (criarModeloLinear):
		MostrarMenu ()

		opcaoSelecionada = input ("Selecione a sua opcao: ")
		print ()

		if (opcaoSelecionada == '0'):
			criarModeloLinear = False

		elif (opcaoSelecionada == '1'):
			print (1)

		elif (opcaoSelecionada == '2'):
			print (2)

		elif (opcaoSelecionada == '3'):
			print (3)

		else:
			print ("Opcao invalida!")

# Chamada da main
main ()
