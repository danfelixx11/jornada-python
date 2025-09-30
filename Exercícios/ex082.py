num = list()
pares = list()
impares = list()
while True:
    n = int(input('Digite um valor: '))
    num.append(n)
    if n % 2 == 0:
        pares.append(n)
    else:
        impares.append(n)
    r = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if r == 'N':
        break
print('-=' * 30)
print(f'Você digitou {len(num)} elementos.')
print(f'A lista de pares é {pares}')
print(f'A lista de ímpares é {impares}')
