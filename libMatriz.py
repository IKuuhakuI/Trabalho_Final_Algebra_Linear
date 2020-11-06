
def criaMatriz(linhas, colunas):
    mat = ['1'] * linhas

    for i in range(linhas):
        mat[i] = ['1'] * colunas

    return mat


def mostraMatriz(mat, linhas):
    for i in range(linhas):
        print(mat[i])


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
