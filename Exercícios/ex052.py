n = int(input('Digite um número: '))
mult = 0
for c in range(2, n - 1):
    if n % c == 0:
        mult += 1
if mult == 0:
    print('É primo')
else:
    print('Não é primo')

