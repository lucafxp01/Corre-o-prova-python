def soma_diagonal_principal(matriz):
    soma = 0
    for i in range(len(matriz)):
        soma += matriz[i][i]
    return soma

""" A resposta correta é a letra A, marquei B. A letra A implementa corretamente,
a funcionalidade de soma dos elementos, da diagonal principal dessa matriz.
"""