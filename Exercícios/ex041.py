from datetime import date
ano_de_nascimento = int(input('Digite o ano de nascimento: '))
ano_atual = date.today().year
idade = ano_atual - ano_de_nascimento
if idade <= 9:
    print('Mirim')
elif idade <= 14:
    print('Infantil')
elif idade <= 19:
    print('Juvenil')
elif idade <= 25:
    print('Adulto')
else:
    print('Master')
    print(f'Idade: {idade} anos')
