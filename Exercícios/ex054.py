pessoa = 0
for cont in range(1, 8):
    idade = int(input(f'Idade da {cont}ª pessoa: '))
    if idade >=21:
        pessoa += 1
print(f'Temos {pessoa} pessoas maiores de idade.')
print(f'Temos {7 - pessoa} pessoas menores de idade.')
