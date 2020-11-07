from libMatriz import MostrarMatriz, GeraMatrizTransposta, MultiplicarMatrizes
from math import sqrt


def ConstruirQTransposto(QMenor, i, j, k)
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
    R = A

    # Matriz Q quadrada nula
    Q = [[0.0] * numeroLinhas for indiceColuna in xrange(numeroLinhas)]

    # Procedimento de Householder (não é feito pra ultimo elemento)
    for indiceColuna in range(numeroLinhas - 1):
        # Cria matriz identidade com mesma dimensão de A (15x15)
        I = [[float(i == j) for i in xrange(numeroLinhas)]
             for j in xrange(numeroLinhas)]

        # Cria o vetor coluna de A (x)
        x = [coluna[indiceColuna] for coluna in coluna[indiceColuna:]]
        e = [coluna[indiceColuna] for coluna in coluna[indiceColuna:]]

        # Cria a norma do vetor coluna com sinal trocado do pivô (alpha)
        alpha = -cmp(x[0], 0) * sqrt(sum([x_i**2 for x_i in x]))

        # Cria hBarra e h (normais ao hiperplano espelho de Householder)
        hBarra = map(lambda p, q: p + alpha * q, x, e)
        normaHBarra = sqrt(sum([x_i**2 for x_i in hBarra]))
        h = map(lambda p: p/normaHBarra, hBarra)

        # Cria a matriz menor QMenor (que aplica a reflexão)
        QMenor = [[float(i == j) - 2.0 * h[i] * v[j]
                   for i in xrange(numeroLinhas-indiceColuna)] for j in xrange(numeroLinhas-indiceColuna)]

        # Preenche a matriz QMenor com elementos da identidade
        QTransposto = [[ConstruirQTransposto(Qmenor,i,j,k) for i in xrange(numeroLinhas)] for j in xrange(numeroLinhas)]

        # Se for a primeira vez (coluna), multiplica por A
        if (indiceColuna == 0)
          Q = QTransposto
          MultiplicarMatrizes(QTransposto, A, R)

        # Se não, multiplica por Q
        else:
          QAuxiliar = []
          MultiplicarMatrizes(QTransposto, Q, QAuxiliar)
          Q = QAuxiliar
          RAuxiliar = []
          MultiplicarMatrizes(QTransposto, R, RAuxiliar)
          R = RAuxiliar

        # Como Q foi definido como o produto de transpostas:
        GeraMatrizTransposta (Q, QAuxiliar)
    return QAuxiliar, R

# matrizCoeficientes -> X^tX onde X é a matriz de dados
# vetorIndependente -> X^tY onde Y é o vetor (lista) de resultados
# Retorno -> w é o vetor (lista) de coeficientes da regressão linear


def ResolverSistema(matrizCoeficientes, vetorIndependente):
