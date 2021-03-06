from libMatriz import MostrarMatriz, GerarMatrizTransposta, MultiplicarMatrizes
from math import sqrt


def ConstruirQTransposto(QMenor, i, j, k):
    if i < k or j < k:
        return float(i == j)
    else:
        return QMenor[i-k][j-k]

# A = QR
# A -> Matriz quadrada X^t X
# Q -> Matriz quadrada ortogonal. Sua transposta multiplicará X^t Y
# R -> Matriz triangular superior que será usada para backcubstitution


def CalcularHouseholder(A):
    # Dimensão da matriz A (15x15 provavelmente)
    numeroLinhas = len(A)

    # Matriz R inicializada igual à A
    R = A.copy()

    # Matriz Q quadrada nula
    Q = [[0.0] * numeroLinhas for indiceColuna in range(numeroLinhas)]

    # Procedimento de Householder (não é feito pra ultimo elemento)
    for indiceColuna in range(numeroLinhas - 1):
        # Cria matriz identidade com mesma dimensão de A (15x15)
        I = [[float(i == j) for i in range(numeroLinhas)]
             for j in range(numeroLinhas)]

        # Cria o vetor coluna de A (x)
        x = [coluna[indiceColuna] for coluna in R[indiceColuna:]]
        e = [coluna[indiceColuna] for coluna in I[indiceColuna:]]

        # Cria a norma do vetor coluna com sinal trocado do pivô (alpha)
        alpha = -((x[0] > 0) - (x[0] < 0)) * sqrt(sum([x_i**2 for x_i in x]))

        # Cria hBarra e h (normais ao hiperplano espelho de Householder)
        hBarra = list(map(lambda p, q: p + alpha * q, x, e))
        normaHBarra = sqrt(sum([x_i**2 for x_i in hBarra]))
        h = list(map(lambda p: p/normaHBarra, hBarra))

        # Cria a matriz menor QMenor (que aplica a reflexão)
        QMenor = [[float(i == j) - 2.0 * h[i] * h[j]
                   for i in range(numeroLinhas-indiceColuna)] for j in range(numeroLinhas-indiceColuna)]

        # Preenche a matriz QMenor com elementos da identidade
        QTransposto = [[ConstruirQTransposto(QMenor, i, j, indiceColuna) for i in range(
            numeroLinhas)] for j in range(numeroLinhas)]

        # Se for a primeira vez (coluna), multiplica por A
        if (indiceColuna == 0):
            Q = QTransposto
            RAuxiliar = []
            MultiplicarMatrizes(QTransposto, A, RAuxiliar)
            R = RAuxiliar

        # Se não, multiplica por Q
        else:
            QAuxiliar = []
            MultiplicarMatrizes(QTransposto, Q, QAuxiliar)
            Q = QAuxiliar
            RAuxiliar = []
            MultiplicarMatrizes(QTransposto, R, RAuxiliar)
            R = RAuxiliar

        QAuxiliar = []
        # Como Q foi definido como o produto de transpostas:
        GerarMatrizTransposta(Q, QAuxiliar)
    return QAuxiliar, R

# matrizCoeficientes -> X^tX onde X é a matriz de dados
# vetorIndependente -> X^tY onde Y é o vetor (lista) de resultados
# Retorno -> w é o vetor (lista) de coeficientes da regressão linear


def ResolverSistema(matrizA, vetorB, vetorIncognitas):
    # Aplica uma decomposição QR por Householder na matriz dos coef. do sistema
    # A x = b
    # Q R x = b 
    Q, R = CalcularHouseholder(matrizA)

    # Calula o transposto da matriz ortogonal que é igual ao seu inverso
    Qt = []
    GerarMatrizTransposta (Q, Qt)

    # Multiplica pelo vetor de termos independentes do sistema
    # Qt Q R x = Qt b
    # I R x = Qt b
    # R x = Qt b
    QtB = []
    MultiplicarMatrizes(Qt, vetorB, QtB)
    
    # Calcula a dimensão de R (deve ser 15x15)
    dimensaoMatrizR = len(R)
    
    # Preenche o vetor de incognitas
    for numeroLinhas in range(dimensaoMatrizR):
        vetorIncognitas.append ([0])

    # Realização da backsubstitution
    # R x = (Qt b)
    # x = ?

    # Varre cada termo do vetor de incógnitas
    for indice in range(dimensaoMatrizR):
        # Começa do termo mais em baixo
        indiceVetorIncognita = dimensaoMatrizR - indice - 1

        S = 0
        # Ex.: dim = 5
        # indice | indiceVetorIncognita | indiceAuxiliar
        #   0               4                   0
        #   1               3                 0 - 1
        #   2               2                 0 - 2
        #   3               1                 0 - 3
        #   4               0                 0 - 4
        for indiceAuxiliar in range (dimensaoMatrizR-1-indiceVetorIncognita):
            # Calcula as operações lineares com os termos ja conhecidos
            S = S + vetorIncognitas[indiceVetorIncognita+indiceAuxiliar+1][0] *            \
            R[indiceVetorIncognita][indiceVetorIncognita+indiceAuxiliar+1]

        # Calcula o próximo termo desconhecido do vetor de incógnitas
        vetorIncognitas[indiceVetorIncognita][0] = (QtB[indiceVetorIncognita][0] - S) /       \
        R[indiceVetorIncognita][indiceVetorIncognita]

    return 0
