print('-=' * 20)
print('Tabuada v.3.0')
print('-=' * 20)
while True:
    num = int(input('Quer ver a tabuada de qual número? '))
    if num < 0:
        break
    print('-' * 20)
    for c in range(1, 11):
        print(f'{num} x {c:2} = {num * c}')
    print('-' * 20)
print('PROGRAMA TABUADA ENCERRADO. Volte sempre!')
print('FIM')
