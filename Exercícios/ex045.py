from random import randint
print('Vamos jogar Jokenpô!')
jogada_usuario = int(input('[0] Pedra\n[1] Papel\n[2] Tesoura\nQual é a sua jogada? '))
jogada_computador = randint(0, 2)
if jogada_usuario == jogada_computador:
    print('Empate!')
elif (jogada_usuario == 0 and jogada_computador == 2) or (jogada_usuario == 1 and jogada_computador == 0) or (jogada_usuario == 2 and jogada_computador == 1):
    print('Você ganhou!')
else:
    print('Você perdeu!')
print(f'Jogada do computador: {jogada_computador}')

# Exercício Python 045: Crie um programa que faça o computador jogar Jokenpô com você.
