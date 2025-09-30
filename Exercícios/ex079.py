numeros = list()
while True:
    n = int(input('Digite um número: '))
    if n not in numeros:
        numeros.append(n)
        print('Número adicionado com sucesso...')
    else:
        print('Número duplicado! Não vou adicionar...')
    r = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if r == 'N':
        break
print('-=' * 30)    
print(f'Você digitou os valores {sorted(numeros)}')
