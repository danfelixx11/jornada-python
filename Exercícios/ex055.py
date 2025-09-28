peso = 0
for cont in range(1, 6):
    peso = float(input(f'Peso da {cont}ª pessoa: '))
    if cont == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print(f'O maior peso lido foi {maior}kg')
print(f'O menor peso lido foi {menor}kg')
