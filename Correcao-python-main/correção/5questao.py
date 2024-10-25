 # Solução 1
  
def tem_duplicados1(lista):
      for i in range(len(lista)):
          for j in range(i + 1, len(lista)):
              if lista[i] == lista[j]:
                  return True
      return False
  # Solução 2

def tem_duplicados2(lista):
      lista_ordenada = sorted(lista)
      for i in range(len(lista_ordenada) - 1):
          if lista_ordenada[i] == lista_ordenada[i + 1]:
              return True
      return False
  # Solução 3
  
def tem_duplicados3(lista):
      elementos_vistos = set()
      for elemento in lista:
          if elemento in elementos_vistos:
              return True
          elementos_vistos.add(elemento)
      return False


""" A resposta correta é a letra C, marquei a D. A solução 3 é mais eficiente pois ela
utiliza uma estrutura auxiliar, o conjunto (set), que armazena elementos já vistos.
"""