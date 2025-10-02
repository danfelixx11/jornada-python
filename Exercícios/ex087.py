matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]] # Lista vazia
spar = mai = scol = 0 # Contadores
for l in range(0, 3): # Laço de 0 a 2
    for c in range(0, 3): # Laço de 0 a 2
        matriz[l][c] = int(input(f'Digite um valor para [{l}, {c}]: ')) # Pergunta o valor
print('-=' * 30) # Quebra de linha
for l in range(0, 3): # Laço de 0 a 2
    for c in range(0, 3): # Laço de 0 a 2
        print(f'[{matriz[l][c]:^5}]', end='') # Mostra o valor
        if matriz[l][c] % 2 == 0: # Se o valor for par
            spar += matriz[l][c] # Soma os valores pares
        if c == 2: # Se a coluna for 2
            scol += matriz[l][c] # Soma os valores da terceira coluna
        if l == 1: # Se a linha for 1
            mai = matriz[l][c] # Atribui o valor da linha 1
            if matriz[l][c] > mai: # Se o valor for maior que o maior valor
                mai = matriz[l][c] # Atribui o valor da linha 1
    print() # Quebra de linha
print(f'A soma dos valores pares é {spar}.') # Mostra a soma dos valores pares
print(f'A soma dos valores da terceira coluna é {scol}.') # Mostra a soma dos valores da terceira coluna
print(f'O maior valor da segunda linha é {mai}.') # Mostra o maior valor da segunda linha
print('-=' * 30) # Quebra de linha
