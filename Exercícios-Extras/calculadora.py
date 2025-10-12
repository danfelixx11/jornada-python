def obter_numero(mensagem):
    """Solicita e valida a entrada de um número."""
    while True:
        try:
            return float(input(mensagem))
        except ValueError:
            print("Por favor, digite um número válido.")

def exibir_menu():
    """Exibe o menu de operações disponíveis."""
    print("\n--- Calculadora Python ---")
    print("Escolha a operação:")
    print("[+] para Soma")
    print("[-] para Subtração")
    print("[*] para Multiplicação")
    print("[/] para Divisão")

def soma(x, y):
    return x + y

def subtracao(x, y):
    return x - y

def multiplicacao(x, y):
    return x * y

def divisao(x, y):
    if y == 0:
        raise ValueError("Não é possível dividir por zero.")
    return x / y

# Dicionário com as operações disponíveis
OPERACOES = {
    '+': {'func': soma, 'nome': 'soma'},
    '-': {'func': subtracao, 'nome': 'subtração'},
    '*': {'func': multiplicacao, 'nome': 'multiplicação'},
    '/': {'func': divisao, 'nome': 'divisão'}
}

def calcular(num1, num2, operacao):
    """Realiza o cálculo com base na operação escolhida."""
    if operacao not in OPERACOES:
        raise ValueError("Operação inválida")
    
    return OPERACOES[operacao]['func'](num1, num2)

def main():
    """Função principal da calculadora."""
    while True:
        exibir_menu()
        
        # Obtendo os números
        num1 = obter_numero("Digite o primeiro número: ")
        num2 = obter_numero("Digite o segundo número: ")
        
        # Obtendo a operação
        operacao = input("Qual operação você deseja realizar? ")
        
        # Realizando o cálculo
        try:
            resultado = calcular(num1, num2, operacao)
            print(f'\nO resultado da {OPERACOES[operacao]["nome"]} entre {num1} e {num2} é: {resultado}')
        except ValueError as erro:
            print(f'\nErro: {erro}')
        except Exception as erro:
            print(f'\nOcorreu um erro inesperado: {erro}')
        
        # Verificando se o usuário quer continuar
        continuar = input('\nDeseja fazer outro cálculo? (s/n): ').lower()
        if continuar != 's':
            print('Obrigado por usar a calculadora. Até mais!')
            break

if __name__ == "__main__":
    main()

