alpha = float(input("informe alpha: "))
print(f"Valor de alpha: {alpha}")

x = float(input("informe X: "))
print(f"Valor de X: {x}")

if alpha > 0.1:
    print("Valor inválido para alpha!")
else:
    if x < 0:
        result = alpha * x
        print(f"Resultado (alpha * x): {result}")
    else:
        print(f"Resultado: {x}")

        """ Esse código é o teste de mesa, basta definir os valores de entrada e seguir as
        operações até verificar o comportamento, do seu programa.
        """