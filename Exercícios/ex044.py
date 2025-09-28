print('====== LOJAS DANIEL ======')
compras = float(input('Qual o valor total das compras? R$ '))
print('''FORMAS DE PAGAMENTO
[1] À vista dinheiro/cheque
[2] À vista cartão
[3] 2x no cartão
[4] 3x ou mais no cartão''')
opção = int(input('Qual é a sua opção? '))
if opção == 1:
    print(f'Sua compra de R$ {compras:.2f} vai custar R$ {compras * 0.9:.2f} no final.')
elif opção == 2:
    print(f'Sua compra de R$ {compras:.2f} vai custar R$ {compras * 0.95:.2f} no final.')
elif opção == 3:
    print(f'Sua compra de R$ {compras:.2f} vai custar R$ {compras:.2f} no final.')
elif opção == 4:
    parcelas = int(input('Quantas parcelas? '))
    if parcelas < 3:
        parcelas = 3
        print('Número de parcelas ajustado para 3.')
    print(f'Sua compra de R$ {compras:.2f} vai custar R$ {compras * 1.2:.2f} no final.')
    print(f'Será parcelada em {parcelas}x de R$ {(compras * 1.2) / parcelas:.2f} COM JUROS.')
else:
    print('Opção inválida de pagamento. Tente novamente!')
    print(f'Sua compra de R$ {compras:.2f} vai custar R$ {compras:.2f} no final.')

# Exercício Python 044: Elabore um programa que calcule o valor a ser pago por um produto,
# considerando o seu preço normal e condição de pagamento:
# à vista dinheiro/cheque: 10% de desconto
# à vista no cartão: 5% de desconto
# 2x no cartão: preço normal
# 3x ou mais no cartão: 20% de juros
