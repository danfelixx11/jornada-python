nome_homem_mais_velho = 0
Mediaidade = 0
sexofeminino20 = 0
for cont in range(1, 6):
    print(f'----- {cont}ª PESSOA -----')
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip().upper()
    Mediaidade += idade
    if cont == 1 and sexo in 'Mm':
        maioridadehomem = idade
        nome_homem_mais_velho = nome
    if sexo in 'Mm' and idade > maioridadehomem:
        maioridadehomem = idade
        nome_homem_mais_velho = nome
    if sexo in 'Ff' and idade < 20:
        sexofeminino20 += 1
Mediaidade /= 4
print(f'A média de idade do grupo é {Mediaidade} anos.')
print(f'O homem mais velho tem {maioridadehomem} anos e se chama {nome_homem_mais_velho}.')
print(f'Temos {sexofeminino20} mulheres com menos de 20 anos.')

