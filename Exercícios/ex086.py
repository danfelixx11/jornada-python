matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]] # Lista vazia
for l in range(0, 3): # Laço de 0 a 2
    for c in range(0, 3): # Laço de 0 a 2
        matriz[l][c] = int(input(f'Digite um valor para [{l}, {c}]: ')) # Pergunta o valor
print('-=' * 30) # Quebra de linha
for l in range(0, 3): # Laço de 0 a 2
    for c in range(0, 3): # Laço de 0 a 2
        print(f'[{matriz[l][c]:^5}]', end='') # Mostra o valor
    print() # Quebra de linha
