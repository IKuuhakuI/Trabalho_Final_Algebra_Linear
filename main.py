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
	matrizIrisSetosaX = []
	matrizIrisSetosaXt= []
	matrizIrisSetosaY = []
	matrizIrisSetosaXtX = []
	matrizIrisSetosaXtY = []
	#Iris-versicolor
	matrizIrisVersicolorX = []
	matrizIrisVersicolorXt= []
	matrizIrisVersicolorY = []
	matrizIrisVersicolorXtX = []
	matrizIrisVersicolorXtY = []
	#Iris-virginica
	matrizIrisVirginicaX = []
	matrizIrisVirginicaXt= []
	matrizIrisVirginicaY = []
	matrizIrisVirginicaXtX = []
	matrizIrisVirginicaXtY = []

	# Leitura do arquivo CSV
	LerCsv (nomeArquivo, linhasArquivo, grupo)
	
	# Separando os dados por tipo de flor
	SepararTipos (linhasArquivo, matrizDadoIrisSetosa, matrizDadoIrisVersicolor, matrizDadoIrisVirginica)

	# Formatando os dados
	# Iris-setosa
	FormatarMatriz (matrizDadoIrisSetosa, matrizIrisSetosaY, matrizIrisSetosaX)
	GerarMatrizTransposta (matrizIrisSetosaX, matrizIrisSetosaXt)	
	# Iris-versicolor
	FormatarMatriz (matrizDadoIrisVersicolor, matrizIrisVersicolorY, matrizIrisVersicolorX)
	GerarMatrizTransposta (matrizIrisVersicolorX, matrizIrisVersicolorXt)	
	# Iris-setosa
	FormatarMatriz (matrizDadoIrisVirginica, matrizIrisVirginicaY, matrizIrisVirginicaX)
	GerarMatrizTransposta (matrizIrisVirginicaX, matrizIrisVirginicaXt)	

	# Multiplicacoes
	# Iris Setosa
	MultiplicarMatrizes (matrizIrisSetosaXt, matrizIrisSetosaY, matrizIrisSetosaXtY)
	MultiplicarMatrizes (matrizIrisSetosaXt, matrizIrisSetosaX, matrizIrisSetosaXtX)
	# Iris Versicolor
	MultiplicarMatrizes (matrizIrisVersicolorXt, matrizIrisVersicolorY, matrizIrisVersicolorXtY)
	MultiplicarMatrizes (matrizIrisVersicolorXt, matrizIrisVersicolorX, matrizIrisVersicolorXtX)
	# Iris Virginica
	MultiplicarMatrizes (matrizIrisVirginicaXt, matrizIrisVirginicaY, matrizIrisVirginicaXtY)
	MultiplicarMatrizes (matrizIrisVirginicaXt, matrizIrisVirginicaX, matrizIrisVirginicaXtX)
	
	while (verificarCriarModeloLinear):
		MostrarMenu ()

		opcaoSelecionada = input ("Selecione a sua opcao: ")
		print ()

		verificarCriarModeloLinear = VerificarOpcao (opcaoSelecionada)	
	
		if (verificarCriarModeloLinear == True):
			if (opcaoSelecionada == '1'):
				print ("Íris Setosa X^t Y: \n")
				MostrarMatriz (matrizIrisSetosaXtY)
				print("Íris Setosa X^t X: \n")
				MostrarMatriz (matrizIrisSetosaXtX)
				print()
			
			elif (opcaoSelecionada == '2'):
				print("Íris Versicolor X^t Y: \n")
				MostrarMatriz (matrizIrisVersicolorXtY)
				print("Íris Versicolor X^t X: \n")
				MostrarMatriz (matrizIrisVersicolorXtX)
				print()

			elif (opcaoSelecionada == '3'):
				print("Íris Virgínica X^t Y: \n")
				MostrarMatriz(matrizIrisVirgínicaXtY)
				print("Íris Virgínica X^t X: \n")
				MostrarMatriz(matrizIrisVirgínicaXtX)
				print()

# Chamada da main
main ()
