print("================================")
print("       CALCULADORA EM PYTHON")
print("================================")

while True:

    print("\nEscolha uma operação:")
    print("1 - Soma")
    print("2 - Subtração")
    print("3 - Multiplicação")
    print("4 - Divisão")
    print("5 - Potenciação")
    print("0 - Sair")

    opcao = input("\nDigite a opção: ")

    if opcao == "0":
        print("\nPrograma encerrado!")
        break

    if opcao in ["1", "2", "3", "4", "5"]:

        numero1 = float(input("Digite o primeiro número: "))
        numero2 = float(input("Digite o segundo número: "))

        if opcao == "1":
            resultado = numero1 + numero2
            print("Resultado:", resultado)

        elif opcao == "2":
            resultado = numero1 - numero2
            print("Resultado:", resultado)

        elif opcao == "3":
            resultado = numero1 * numero2
            print("Resultado:", resultado)

        elif opcao == "4":
            if numero2 == 0:
                print("Erro: não é possível dividir por zero.")
            else:
                resultado = numero1 / numero2
                print("Resultado:", resultado)

        elif opcao == "5":
            resultado = numero1 ** numero2
            print("Resultado:", resultado)

    else:
        print("Opção inválida. Tente novamente.")
        