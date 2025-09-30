'''num = [2, 5, 9, 1] # Lista
num[2] = 3  # Alterando valor do índice 2
num.append(7) # Adicionando valor no final da lista
num.sort(reverse=True) # Ordenando a lista em ordem decrescente
num.insert(2, 0) # Adicionando valor 0 no índice 2
num.pop(2) # Removendo o valor do índice 2
if 5 in num:
    num.remove(5) # Removendo o valor 5 da lista
else:
    print('Não achei o número 5') # Mensagem caso o valor 5 não esteja na lista
print(num) # Imprimindo a lista
print(f'Essa lista tem {len(num)} elementos.') # Imprimindo o tamanho da lista'''

'''valores = []
valores.append(5)
valores.append(9)
valores.append(4)

for c, v in enumerate(valores):
    print(f'Na posição {c} encontrei o valor {v}!')
print('Cheguei ao final da lista.')'''

'''valores = list()
for cont in range(0, 5):
    valores.append(int(input('Digite um valor: ')))
for c, v in enumerate(valores):
    print(f'Na posição {c} encontrei o valor {v}!')
print('Cheguei ao final da lista.')'''

a = [2, 3, 4, 7] # Lista A
b = a # Lista B
b[2] = 8 # Alterando o valor do índice 2 da lista B
print(f'Lista A: {a}')
print(f'Lista B: {b}')
# Obs: Ao alterar a lista B, a lista A também é alterada, pois ambas apontam para o mesmo local na memória.

c = a[:] # Lista C (cópia da lista A)
c[2] = 8 # Alterando o valor do índice 2 da lista C
print(f'Lista C: {c}')
# Obs: Ao alterar a lista C, a lista A não é alterada, pois a lista C é uma cópia independente da lista A.
# Obs: Para criar uma cópia de uma lista, deve-se usar o slicing [:].
