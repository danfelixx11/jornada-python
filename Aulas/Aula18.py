'''teste =  []
teste.append('Daniel')
teste.append(40)
galera = list()
galera.append(teste[:])
teste[0] = 'Maria'
teste[1] = 22
galera.append(teste[:])
print(galera)'''

'''galera = [['Daniel', 40],['Melissa', 39], ['Marina', 11], ['Lorenzo', 11]]
for p in galera:
    print(f'{p[0]} tem {p[1]} anos de idade.')'''

galera = [] # Lista vazia
dado = [] # Lista vazia
totmai = totmen = 0 # Contadores de maiores e menores de idade
for c in range(0, 5): # Laço de 0 a 4
    dado.append(str(input('Nome: '))) # Adiciona o nome na lista
    dado.append(int(input('Idade: '))) # Adiciona a idade na lista
    galera.append(dado[:]) # Adiciona a lista dentro da lista
    dado.clear() # Limpa a lista

for p in galera: # Laço para percorrer a lista
    if p[1] >= 21: # Se a idade for maior ou igual a 21
        print(f'{p[0]} é maior de idade.') # Mostra o nome e a idade
        totmai += 1 # Incrementa o contador de maiores de idade
    else:
        print(f'{p[0]} é menor de idade.') # Mostra o nome e a idade
        totmen += 1 # Incrementa o contador de menores de idade
print(f'Temos {totmai} maiores de idade e {totmen} menores de idade.') # Mostra o total de maiores e menores de idade

# Fim do programa
