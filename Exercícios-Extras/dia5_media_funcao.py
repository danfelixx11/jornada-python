# --- Construção da nossa "Ferramenta" ---
def calcula_media(a, b, c):
    """Esta função recebe três números, calcula e retorna a média."""
    soma = a + b + c
    media = soma / 3
    return media

# --- Usando a "Ferramenta" que criamos ---
print('--- Calculadora de Média de 3 Números ---')

num1 = int(input('Digite o primeiro número: '))
num2 = int(input('Digite o segundo número: '))
num3 = int(input('Digite o terceiro número: '))

# Aqui estamos "chamando" a função e guardando o resultado dela
resultado_final = calcula_media(num1, num2, num3)

print(f'A média dos números é: {resultado_final:.2f}')

