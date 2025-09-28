soma = 0
for num in range(1, 7):
    n = int(input(f'Digite o {num}º valor: '))
    if n % 2 == 0:
        soma = soma + n
print(f'Você digitou {num} números, e a soma dos números PARES é {soma}.')
