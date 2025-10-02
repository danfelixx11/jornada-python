from random import randint # Importa a biblioteca random para gerar números aleatórios
from time import sleep # Importa a biblioteca time para pausar o programa
lista = [] # Lista vazia
jogo = [] # Lista vazia
print('-' * 30) # Quebra de linha
print('     JOGO DA MEGA SENA     ') # Mostra o título
print('-' * 30) # Quebra de linha
jogos = int(input('Quantos jogos você quer que eu sorteie? ')) # Pergunta quantos jogos você quer que eu sorteie
print('-' * 30) # Quebra de linha
tot = 1 # Contador
while tot <= jogos: # Enquanto o contador for menor que o número de jogos
    cont = 0 # Contador
    while True: # Enquanto o contador for menor que 6
        num = randint(0, 60) # Gera um número aleatório entre 0 e 60
        if num not in lista: # Se o número não estiver na lista
            lista.append(num) # Adiciona o número na lista
            cont += 1 # Incrementa o contador
        if cont == 6: # Se o contador for igual a 6
            break # Sai do loop
    lista.sort() # Ordena a lista
    jogo.append(lista[:]) # Adiciona a lista dentro da lista
    lista.clear() # Limpa a lista
    tot += 1 # Incrementa o contador
print('-=' * 3, f'SORTEANDO {jogos} JOGOS', '-=' * 3) # Mostra o título
for i, l in enumerate(jogo):  # Mostra os jogos
    print(f'Jogo {i+1}: {l}') # Mostra o jogo
    sleep(1) # Pausa de 1 segundo
    print('-' * 30) # Mostra a linha
print('BOA SORTE!') # Mostra a mensagem de boa sorte
