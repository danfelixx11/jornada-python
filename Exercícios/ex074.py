from random import randint
n = (randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10))
print(f'Os números sorteados foram: {n}')
print(f'O maior número sorteado foi: {max(n)}')
print(f'O menor número sorteado foi: {min(n)}')
print('-'*40)
