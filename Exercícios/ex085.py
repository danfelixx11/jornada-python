num = [[], []] # Lista vazia
for c in range(1, 8): # Laço de 1 a 7
    valor = int(input(f'Digite o {c}º valor: ')) # Pergunta o valor
    if valor % 2 == 0: # Se o valor for par
        num[0].append(valor) # Adiciona o valor na lista de pares
    else:
        num[1].append(valor) # Adiciona o valor na lista de ímpares
num[0].sort() # Ordena a lista de pares
num[1].sort() # Ordena a lista de ímpares
print(f'Os valores pares digitados foram: {num[0]}') # Mostra a lista de pares
print(f'Os valores ímpares digitados foram: {num[1]}') # Mostra a lista de ímpares
