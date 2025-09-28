valor_da_casa = float(input('Qual o valor da casa? R$ '))
salario = float(input('Qual o salário do comprador? R$ '))
anos = int(input('Em quantos anos ele vai pagar? '))
prestacao = valor_da_casa / (anos * 12)
print(f'Para pagar uma casa de R$ {valor_da_casa:.2f} em {anos} anos', end='')
print(f' a prestação será de R$ {prestacao:.2f}')
if prestacao <= salario * 0.3:
    print('Empréstimo pode ser CONCEDIDO!')
else:
    print('Empréstimo pode ser NEGADO!')
    print('O valor da prestação ultrapassa 30% do salário.')
    valor_necessario = prestacao - (salario * 0.3)
    print(f'Você precisa de R$ {valor_necessario:.2f} a mais para pagar essa casa.')
