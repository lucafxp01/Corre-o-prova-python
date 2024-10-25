""" LETRA A) Calcule e informe o IMC da pessoa.
"""
altura = float(input("Digite sua altura em metros(M): "))
peso = float(input("Digite seu peso em quilograma(KG): "))
imc = peso / (altura ** 2)
print("Seu indice de massa corporal é de: {:.2f}".format(imc))

