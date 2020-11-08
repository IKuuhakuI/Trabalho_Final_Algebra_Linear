from libFormatar import LerCsv, SepararTipos, FormatarMatriz
from libMenu import MostrarMenu, VerificarOpcao

def main ():
	# Controles do Menu
	verificarCriarModeloLinear = True
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
	
	while (verificarCriarModeloLinear):
		MostrarMenu ()

		opcaoSelecionada = input ("Selecione a sua opcao: ")
		print ()

		verificarCriarModeloLinear = VerificarOpcao (opcaoSelecionada)	
	
		if (verificarCriarModeloLinear == True):
			pass			

# Chamada da main
main ()
