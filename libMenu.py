def MostrarMenu ():
	print ()

	print ("1- Calcular modelo linear para a Iris-setosa")
	print ("2- Calcular modelo linear para a Iris-versicolor")
	print ("3- Calcular modelo linear para a Iris-virginica")
	print ("O- Sair do programa")
	print ()

def VerificarOpcao (opcaoSelecionada):

	criarModeloLinear = True

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

	return criarModeloLinear

