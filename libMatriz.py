import csv

def criaMatriz(linhas, colunas):
    mat = ['1'] * linhas

    for i in range(linhas):
        mat[i] = ['1'] * colunas

    return mat


def mostraMatriz(mat, linhas):
    for i in range(linhas):
        print (mat[i])


def transposta(mat, linhas, colunas):

    transposta = criaMatriz(linhas, colunas)

    for i in range(linhas):
        for j in range(colunas):
            transposta[i][j] = mat[j][i]

    return transposta


def multiplica(matA, matB, linA, colA, colB):

    resultado = criaMatriz(linA, colB)

    for i in range(linA):
        for k in range(colB):
            soma = 0
            for j in range(colA):
                soma = soma + matA[i][j] * matB[j][k]
            resultado[i][k] = soma

    return resultado

def geraMatriz(inicio, fim):

    with open("iris.csv") as csv_file:

        csv_reader = csv.reader(csv_file, delimiter=",")
        matriz = criaMatriz(4, 15)
        colunas = inicio - 1
        intervalo = fim - colunas

        for conteudo in csv_reader:
            contaLinha = 0

            while  contaLinha < 4:

                if(colunas < intervalo):
                    matriz[contaLinha][colunas] = conteudo[contaLinha]

                    if(contaLinha == 2):
                        matriz[contaLinha][colunas] = conteudo[contaLinha + 1]
                        break

                contaLinha = contaLinha + 1
            colunas = colunas + 1

    return matriz

def geraMatrizResultado(inicio, fim):

    with open("iris.csv") as csv_file:

        csv_reader = csv.reader(csv_file, delimiter=",")
        colunas = inicio - 1
        intervalo = fim - colunas
        linhasResultado = 0
        resultado = criaMatriz(15, 1)

        for conteudo in csv_reader:
            contaLinha = 0
            while  contaLinha < 4:

                if(colunas < intervalo):

                    if(contaLinha == 2):

                        resultado[linhasResultado] = conteudo[contaLinha]
                        linhasResultado = linhasResultado + 1
                        break

                contaLinha = contaLinha + 1
            colunas = colunas + 1

    return resultado
