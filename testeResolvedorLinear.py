from libMatriz import MostrarMatriz
from libResolvedorLinear import CalcularHouseholder, ResolverSistema

A = [[12, -51, 4], [6, 167, -68], [-4, 24, -41]]

Q, R = CalcularHouseholder(A)

print("A:")
MostrarMatriz(A)

print("Q")
MostrarMatriz(Q)

print("R")
MostrarMatriz(R)

print ("\n\n------ PARTE 2 -------\n\n")

b = [[35], [430], [-56]]
x = []

ResolverSistema(A, b, x)

print ("Matriz A")
MostrarMatriz (A)

print ("Vetor b")
MostrarMatriz(b)

print ("Vetor x (calculado)")
MostrarMatriz(x)