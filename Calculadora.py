print("================================")
print("       CALCULADORA EM PYTHON")
print("================================")

historico = []

while True:

    print("\nEscolha uma operação:")
    print("1 - Soma")
    print("2 - Subtração")
    print("3 - Multiplicação")
    print("4 - Divisão")
    print("5 - Potenciação")
    print("6 - Ver histórico")
    print("0 - Sair")

    opcao = input("\nDigite a opção: ")

    if opcao == "0":
        print("\nPrograma encerrado!")
        break

    if opcao == "6":
        print("\n===== HISTÓRICO =====")

        if len(historico) == 0:
            print("Nenhuma operação realizada.")
        else:
            for operacao in historico:
                print(operacao)

        continue

    if opcao in ["1", "2", "3", "4", "5"]:

        numero1 = float(input("Digite o primeiro número: "))
        numero2 = float(input("Digite o segundo número: "))

        if opcao == "1":
            resultado = numero1 + numero2
            operacao = f"{numero1} + {numero2} = {resultado}"

        elif opcao == "2":
            resultado = numero1 - numero2
            operacao = f"{numero1} - {numero2} = {resultado}"

        elif opcao == "3":
            resultado = numero1 * numero2
            operacao = f"{numero1} x {numero2} = {resultado}"

        elif opcao == "4":
            if numero2 == 0:
                print("Erro: não é possível dividir por zero.")
                continue

            resultado = numero1 / numero2
            operacao = f"{numero1} / {numero2} = {resultado}"

        elif opcao == "5":
            resultado = numero1 ** numero2
            operacao = f"{numero1} ^ {numero2} = {resultado}"

        print("Resultado:", resultado)

        historico.append(operacao)

    else:
        print("Opção inválida. Tente novamente.")