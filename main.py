from libFormatar import LerCsv, SepararTipos, FormatarMatriz, MostrarModelo
from libMatriz import GerarMatrizTransposta, MultiplicarMatrizes, MostrarMatriz
from libMenu import MostrarMenu, VerificarOpcao
from libResolvedorLinear import ResolverSistema

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

	# Coeficientes de cada flor
	coeficientesIrisSetosa = []
	coeficientesIrisVersicolor = []
	coeficientesIrisVirginica = []

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
				ResolverSistema(matrizIrisSetosaXtX, matrizIrisSetosaXtY,
				coeficientesIrisSetosa)
				print("------------------------------------------------------------------------------------")
				#MostrarMatriz(coeficientesIrisSetosa)

				print("\nModelo Linear da Íris Setosa: \n")
				
				MostrarModelo (coeficientesIrisSetosa)
				#print("PL = " + str(coeficientesIrisSetosa[0][0]) + " SL + " \
				#							+ str(coeficientesIrisSetosa[1][0]) + " SW + " \
				#							+ str(coeficientesIrisSetosa[2][0]) + " PW + " \
				#							+ str(coeficientesIrisSetosa[3][0]))
				print()
				print("Onde:")
				print("PL - Comprimento da pétala em cm")
				print("SL - Comprimento da sépala em cm")
				print("SW - Largura da sépala em cm")
				print("PW - Largura da pétala em cm")
				print()
				print("------------------------------------------------------------------------------------\n")
			
			elif (opcaoSelecionada == '2'):
				ResolverSistema(matrizIrisVersicolorXtX, matrizIrisVersicolorXtY,
				coeficientesIrisVersicolor)
				print("------------------------------------------------------------------------------------")
				print("\nModelo Linear da Íris Versicolor: \n")
	
				MostrarModelo (coeficientesIrisVersicolor)
				#print("PL = " + str(coeficientesIrisVersicolor[0][0]) + " SL + " \
				#							+ str(coeficientesIrisVersicolor[1][0]) + " SW + " \
				#							+ str(coeficientesIrisVersicolor[2][0]) + " PW + " \
				#							+ str(coeficientesIrisVersicolor[3][0]))
				print()
				print("Onde:")
				print("PL - Comprimento da pétala em cm")
				print("SL - Comprimento da sépala em cm")
				print("SW - Largura da sépala em cm")
				print("PW - Largura da pétala em cm")
				print()
				print("------------------------------------------------------------------------------------\n")

			elif (opcaoSelecionada == '3'):
				
				ResolverSistema(matrizIrisVirginicaXtX, matrizIrisVirginicaXtY,
				coeficientesIrisVirginica)
				print("------------------------------------------------------------------------------------")
				print("\nModelo Linear da Íris Virgínica: \n")

				MostrarModelo (coeficientesIrisVirginica)				
	
				#print("PL = " + str(coeficientesIrisVirginica[0][0]) + " SL + " \
				#							+ str(coeficientesIrisVirginica[1][0]) + " SW + " \
				#							+ str(coeficientesIrisVirginica[2][0]) + " PW + " \
				#							+ str(coeficientesIrisVirginica[3][0]))
				print()
				print("Onde:")
				print("PL - Comprimento da pétala em cm")
				print("SL - Comprimento da sépala em cm")
				print("SW - Largura da sépala em cm")
				print("PW - Largura da pétala em cm")
				print()
				print("------------------------------------------------------------------------------------\n")
			
			else:
				print("------------------------------------------------------------------------------------\n")
				print ("Opcao invalida!")
				print ()
				print("------------------------------------------------------------------------------------\n")

# Chamada da main
main ()
