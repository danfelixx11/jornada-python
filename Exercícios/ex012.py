produto = float(input('Qual o preço do seu produto?: R$ '))
porcentagem = int(input('Porcentagem de desconto?: '))
desconto = (produto / 100) * porcentagem
total = produto - desconto
print(f'Valor de {porcentagem} % desconto: R$ {desconto:.2f}')
print(f'Valor final do produto: R$ {total:.2f}')
