def calculadora():
    while True:
        # Exibindo o menu de operações
        print("\nEscolha a operação:")
        print("1: Soma")
        print("2: Subtração")
        print("3: Multiplicação")
        print("4: Divisão")
        print("0: Sair")

        # Capturando a opção do usuário
        opcao = input("Digite o número para a operação correspondente: ")

        # Verificando a opção de saída
        if opcao == "0":
            print("Saindo do programa...")
            break

        # Verificando se a opção é válida
        if opcao not in ["1", "2", "3", "4"]:
            print("Essa opção não existe")
            continue

        # Capturando os números para a operação
        try:
            num1 = float(input("Digite o primeiro valor: "))
            num2 = float(input("Digite o segundo valor: "))
        except ValueError:
            print("Entrada inválida! Digite números válidos.")
            continue

        # Realizando a operação escolhida
        if opcao == "1":
            resultado = num1 + num2
            print(f"Resultado da Soma: {resultado}")
        elif opcao == "2":
            resultado = num1 - num2
            print(f"Resultado da Subtração: {resultado}")
        elif opcao == "3":
            resultado = num1 * num2
            print(f"Resultado da Multiplicação: {resultado}")
        elif opcao == "4":
            if num2 == 0:
                print("Erro: Divisão por zero!")
            else:
                resultado = num1 / num2
                print(f"Resultado da Divisão: {resultado}")

# Chamando a função calculadora
calculadora()
