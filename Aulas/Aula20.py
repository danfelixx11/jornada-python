def mensagem(msg): # Função com parâmetro
    print('-' * 30)
    print(msg)
    print('-' * 30)


mensagem('Curso em Vídeo')

def texto(): # Função sem parâmetro
    print('-' * 30)

texto()
print('Sua mensagem aqui')
texto()


def soma(a,b):
    s = a + b
    print(s)

soma(4,5)
soma(8,9)
soma(2,1)

def contador(*num):
    for valor in num:
        print(F'{valor} ', end='')
    print('FIM')


contador(2, 1, 7)


def dobra(lst):
    pos = 0
    while pos < len(lst):
        lst[pos] *= 2
        pos += 1


valores = [6, 3, 9, 1, 0, 2]        
dobra(valores)
print(valores)

def soma(*valores):
    s =  0
    for num in valores:
        s+= num
    print(f'Somando os valores {valores} temos {s}')

soma(5,2)
soma(2, 9, 4)

