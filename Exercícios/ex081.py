valores = [] # Lista vazia
while True: # Laço infinito
    valores.append(int(input('Digite um valor: '))) # Adiciona valor na lista
    r = str(input('Quer continuar? [S/N] ')).strip().upper()[0] # Pergunta se quer continuar
    if r == 'N': # Se a resposta for N, sai do laço
        break # Sai do laço
print('-=' * 30)
print(f'Você digitou {len(valores)} elementos.') # Mostra quantos elementos foram digitados
valores.sort(reverse=True) # Ordena a lista em ordem decrescente
print(f'Os valores em ordem decrescente são {valores}') # Mostra a lista ordenada
if 5 in valores: # Verifica se o valor 5 está na lista
    print('O valor 5 faz parte da lista!') # Se estiver, mostra essa mensagem
else: # Se não estiver, mostra essa mensagem
    print('O valor 5 não foi encontrado na lista!') # Se não estiver, mostra essa mensagem
# Obs: A função sort() ordena a lista. Se o parâmetro reverse=True for usado, a lista é ordenada em ordem decrescente.

