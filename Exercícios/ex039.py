from datetime import date
ano_de_nascimento = int(input('Digite o ano de nascimento: '))
ano_atual = date.today().year
idade = ano_atual - ano_de_nascimento
print(f'A sua idade é {idade} anos.')
if idade < 18:
    saldo = 18 - idade
    ano = ano_atual + saldo
    print(f'Ainda faltam {saldo} anos para o alistamento.')
    print(f'Seu alistamento será em {ano}.')
elif idade == 18:
    print('Você tem que se alistar IMEDIATAMENTE!')
else:
    saldo = idade - 18
    ano = ano_atual - saldo
    print(f'Você já deveria ter se alistado há {saldo} anos.')
    print(f'Seu alistamento foi em {ano}.')
