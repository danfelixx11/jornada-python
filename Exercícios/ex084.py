temp = [] # Lista vazia
princ = [] # Lista vazia

while True: # Laço infinito
    temp.append(str(input('Nome: '))) # Adiciona o nome na lista
    temp.append(float(input('Peso: '))) # Adiciona o peso na lista
    princ.append(temp[:]) # Adiciona a lista dentro da lista
    temp.clear() # Limpa a lista
    r = str(input('Quer continuar? [S/N] ')).strip().upper()[0] # Pergunta se quer continuar
    if r == 'N': # Se a resposta for N, sai do laço
        break # Sai do laço
print(f'Ao todo, você cadastrou {len(princ)} pessoas.') # Mostra o total de pessoas cadastradas
print(f'O maior peso foi {max(princ)[1]}kg. Peso de {max(princ)[0]}.') # Mostra o maior peso e o nome da pessoa
print(f'O menor peso foi {min(princ)[1]}kg. Peso de {min(princ)[0]}.') # Mostra o menor peso e o nome da pessoa

# Fim do programa
