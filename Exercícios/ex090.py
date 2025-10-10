aluno = dict() # Dicionário vazio
aluno['nome'] = str(input('Nome: ')) # Adiciona o nome no dicionário
aluno['media'] = float(input(f'Média de {aluno["nome"]}: ')) # Adiciona a média no dicionário
if aluno['media'] >= 7: # Se a média for maior ou igual a 7
    aluno['situação'] = 'Aprovado' # Adiciona a situação no dicionário
elif 5 <= aluno['media'] < 7: # Se a média for maior ou igual a 5 e menor que 7
    aluno['situação'] = 'Recuperação' # Adiciona a situação no dicionário
else: # Se a média for menor que 5
    aluno['situação'] = 'Reprovado' # Adiciona a situação no dicionário
print('-=' * 30) # Imprime 30 traços
for k, v in aluno.items(): # Laço para percorrer o dicionário
    print(f'{k} é igual a {v}') # Imprime o nome e a média
print('-=' * 30) # Imprime 30 traços
