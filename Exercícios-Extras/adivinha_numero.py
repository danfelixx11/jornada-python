import random # Importa a biblioteca random para gerar números aleatórios
numero_secreto = random.randint(1, 10) # Gera um número aleatório entre 1 e 10
print('--- Jogo de Adivinhação ---')
print('Eu pensei em um número entre 1 e 10. Tente adivinhar!')

# Inicializa a variável de tentativa
palpite = 0 # Começamos com um palpite que não seja o número
tentativas = 0 # Contador para o número de tentativas

# Condição de teste: O jogo continua Equanto o palpite for diferente do número secreto
while palpite != numero_secreto:
    palpite = int(input('Qual é o seu palpite? ')) # Solicita um palpite ao usuário
    tentativas += 1 # Incrementa o contador de tentativas

    #Bloco de condições dentro do loop para dar dicas
    if palpite < numero_secreto:
        print('Muito baixo! Tente um número maior.')
    elif palpite > numero_secreto:
        print('Muito alto! Tente um número menor.')
    else:
        print(f'Parabéns! Você adivinhou o número {numero_secreto} em {tentativas} tentativas.')
print('--- Fim do Jogo ---')
