ficha = [] # Lista vazia

while True: # Laço infinito
    nome = str(input('Nome: ')) # Pergunta o nome
    nota1 = float(input('Nota 1: ')) # Pergunta a primeira nota
    nota2 = float(input('Nota 2: ')) # Pergunta a segunda nota
    media = (nota1 + nota2) / 2 # Calcula a média
    ficha.append([nome, [nota1, nota2], media]) # Adiciona o nome, as notas e a média na lista
    r = str(input('Quer continuar? [S/N] ')).strip().upper()[0] # Pergunta se quer continuar
    if r == 'N': # Se a resposta for N, sai do laço
        break # Sai do laço

print('-' * 30) # Mostra a linha
print(f'{"No.":<4}{"NOME":<10}{"MÉDIA":>8}') # Mostra o cabeçalho
print('-' * 26) # Mostra a linha

for i, a in enumerate(ficha): # Mostra os alunos e as notas
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}') # Mostra o nome, as notas e a média

while True: # Laço infinito
    print('-' * 30) # Mostra a linha
    opc = int(input('Mostrar notas de qual aluno? (999 interrompe): ')) # Pergunta qual aluno mostrar as notas
    if opc == 999: # Se a resposta for 999, sai do laço
        break # Sai do laço
    if opc <= len(ficha) - 1: # Se a resposta for menor ou igual ao número de alunos, mostra as notas
        print(f'Notas de {ficha[opc][0]} são {ficha[opc][1]}') # Mostra o nome e as notas
        
print('FINALIZANDO...') # Mostra a mensagem de finalização
print('<<< VOLTE SEMPRE >>>') # Mostra a mensagem de volta
