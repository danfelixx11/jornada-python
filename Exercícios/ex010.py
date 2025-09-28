carteira = float(input('Quanto dinheiro tenho na Carteira?: R$ '))
dolar = float(input('Insira a cotação atual do Dolar: $ '))
compra = carteira / dolar
print(f'Você pode comprar: $ {compra:.2f}')
if dolar <= 0: print("Cotação inválida!")
