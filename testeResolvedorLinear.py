from libMatriz import MostrarMatriz
from libResolvedorLinear import CalcularHouseholder

A = [[12, -51, 4], [6, 167, -68], [-4, 24, -41]]

Q, R = CalcularHouseholder(A)

print("A:")
MostrarMatriz(A)

print("Q")
MostrarMatriz(Q)

print("R")
MostrarMatriz(R)
