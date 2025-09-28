# Iniciamos um loop "infinito" que só será quebrado quando o usuário decidir sair.
while True:
    print("\n--- Calculadora Python ---")

    # Etapa 1: Obter os números do usuário
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))

    # Etapa 2: Obter a operação desejada
    print("Escolha a operação:")
    print("[+] para Soma")
    print("[-] para Subtração")
    print("[*] para Multiplicação")
    print("[/] para Divisão")
    operacao = input("Qual operador você deseja realizar? ")

    # Etapa 3: Usar if/elif/else para calcular e mostrar o resultado
    if operacao == '+':
        resultado = num1 + num2
        print(f'O resuldado de {num1} + {num2} é: {resultado}')
    elif operacao == '-':
        resultado = num1 - num2
        print(f'O resultado de {num1} - {num2} é: {resultado}')
    elif operacao == '*':
        resultado = num1 * num2
        print(f'O resultado de {num1} * {num2} é: {resultado}')
    elif operacao == '/':
        # Verificação especial para evitar divisão por zero, um erro comum!
        if num2 == 0:
            print('Erro: Não é possível dividir por zero.')
        else:
            resultado = num1 / num2
            print(f'O resultado de {num1} / {num2} é: {resultado}')
    else:
        # Caso o usuário digite uma operação inválida
        print('Operação inválida. Por favor, tente novamente.')
    
    # Etapa 4 (Extra): Perguntar se o usuário quer continuar
    continuar = input('\nDeseja fazer outro cálculo? (s/n): ')
    if continuar.lower() != 's':
        print('Obrigado por usar a calculadora. Até mais!')
        break # Este comando quebra o loop 'While' e encerra o programa.

