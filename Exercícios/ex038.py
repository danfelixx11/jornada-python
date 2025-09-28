num1 = int(input('Digite o primeiro número: '))
num2 = int(input('Digite o segundo número: '))
if num1 > num2:
    print(f'O PRIMEIRO valor ({num1}) é maior.')
elif num2 > num1:
    print(f'O SEGUNDO valor ({num2}) é maior.')
else:
    print('Os dois valores são iguais.')
