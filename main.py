from libFormatar import LerCsv, SepararTipos, FormatarMatriz
from libMatriz import GerarMatrizTransposta, MultiplicarMatrizes, MostrarMatriz
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
	matrizIrisSetosaDependenteTransposta= []
	matrizIrisSetosaIndependente = []
	multiplicaIrisSetosaTranspostaIndependente = []
	multiplicaIrisSetosaTranspostaDependente = []
	#Iris-versicolor
	matrizIrisVersicolorDependente = []
	matrizIrisVersicolorDependenteTransposta= []
	matrizIrisVersicolorIndependente = []
	multiplicaIrisVersicolorTranspostaIndependente = []
	multiplicaIrisVersicolorTranspostaDependente = []
	#Iris-virginica
	matrizIrisVirginicaDependente = []
	matrizIrisVirginicaDependenteTransposta= []
	matrizIrisVirginicaIndependente = []
	multiplicaIrisVirginicaTranspostaIndependente = []
	multiplicaIrisVirginicaTranspostaDependente = []

	# Leitura do arquivo CSV
	LerCsv (nomeArquivo, linhasArquivo, grupo)
	
	# Separando os dados por tipo de flor
	SepararTipos (linhasArquivo, matrizDadoIrisSetosa, matrizDadoIrisVersicolor, matrizDadoIrisVirginica)

	# Formatando os dados
	# Iris-setosa
	FormatarMatriz (matrizDadoIrisSetosa, matrizIrisSetosaIndependente, matrizIrisSetosaDependente)
	GerarMatrizTransposta (matrizIrisSetosaDependente, matrizIrisSetosaDependenteTransposta)	
	# Iris-versicolor
	FormatarMatriz (matrizDadoIrisVersicolor, matrizIrisVersicolorIndependente, matrizIrisVersicolorDependente)
	GerarMatrizTransposta (matrizIrisVersicolorDependente, matrizIrisVersicolorDependenteTransposta)	
	# Iris-setosa
	FormatarMatriz (matrizDadoIrisVirginica, matrizIrisVirginicaIndependente, matrizIrisVirginicaDependente)
	GerarMatrizTransposta (matrizIrisVirginicaDependente, matrizIrisVirginicaDependenteTransposta)	

	# Multiplicacoes
	# Iris Setosa
	MultiplicarMatrizes (matrizIrisSetosaDependenteTransposta, matrizIrisSetosaIndependente, multiplicaIrisSetosaTranspostaIndependente)
	MultiplicarMatrizes (matrizIrisSetosaDependenteTransposta, matrizIrisSetosaDependente, multiplicaIrisSetosaTranspostaDependente)
	# Iris Versicolor
	MultiplicarMatrizes (matrizIrisVersicolorDependenteTransposta, matrizIrisVersicolorIndependente, multiplicaIrisVersicolorTranspostaIndependente)
	MultiplicarMatrizes (matrizIrisVersicolorDependenteTransposta, matrizIrisVersicolorDependente, multiplicaIrisVersicolorTranspostaDependente)
	# Iris Virginica
	MultiplicarMatrizes (matrizIrisVirginicaDependenteTransposta, matrizIrisVirginicaIndependente, multiplicaIrisVirginicaTranspostaIndependente)
	MultiplicarMatrizes (matrizIrisVirginicaDependenteTransposta, matrizIrisVirginicaDependente, multiplicaIrisVirginicaTranspostaDependente)
	
	while (verificarCriarModeloLinear):
		MostrarMenu ()

		opcaoSelecionada = input ("Selecione a sua opcao: ")
		print ()

		verificarCriarModeloLinear = VerificarOpcao (opcaoSelecionada)	
	
		if (verificarCriarModeloLinear == True):
			if (opcaoSelecionada == '1'):
				MostrarMatriz (multiplicaIrisSetosaTranspostaIndependente)
			
			elif (opcaoSelecionada == '2'):
				MostrarMatriz (multiplicaIrisVersicolorTranspostaIndependente)

			elif (opcaoSelecionada == '3'):
				MostrarMatriz (multiplicaIrisVirginicaTranspostaIndependente)
# Chamada da main
main ()
