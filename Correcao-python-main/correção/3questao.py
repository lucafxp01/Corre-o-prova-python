def func(n):
  if n == 0:
    return 1
  else:
    return n * func(n - 1)

print(func(3))
""" A resposta correta é a letra B (6). Marquei a letra A. Esse código tem a saida 6, pois
ele calcula o fatoriaL de 3.
"""