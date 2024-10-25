altura = float(input("Digite sua altura em metros(M): \n"))
peso = float(input("Digite seu peso em quilograma(KG): \n"))
imc = peso / (altura ** 2)
print("Seu indice de massa corporal é de: {:.2f}" .format(imc))

if imc < 17:
  print("Você está muito abaixo do peso! \n")
elif imc >= 17 and imc < 18.6:
  print("Você está abaixo do peso! \n")
elif imc >= 18.6 and imc < 26:
  print("Você está com o peso normal! \n")
elif imc >= 26 and imc < 31:
  print("Você está com sobrepeso! \n")
elif imc >= 31 and imc < 36:
  print("Você está com obesidade Grau 1! \n")
elif imc >= 36 and imc < 41:
  print("Você está com obesidade Grau 2! \n")
elif imc >= 40:
  print("Você está com obesidade Grau 3! \n Vai para uma academia seu projeto de baleia mórbida! \n")


  """ Esse programa informa o IMC da pessoa e a sua classificação conforme (OMS).
  """