listagem = ('Pão', 1, 'Leite', 4.5, 'Arroz', 15.99, 'Feijão', 7.80, 'Carne', 25.00, 'Frango', 12.30, 'Macarrão', 5.50)
print('-'*40)
print(f'{"LISTA DE PREÇOS":^40}')
print('-'*40)
for pos in range(0, len(listagem)):
    if pos % 2 == 0:
        print(f'{listagem[pos]:.<30}', end='')
    else:
        print(f'R$ {listagem[pos]:>7.2f}')
print('-'*40)
