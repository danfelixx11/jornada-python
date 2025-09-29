valores = ()
cont = 0
pares = ()
for n in range(4):
    numero = int(input('Digite um número: '))
    valores += (numero,)
    if 9 >= numero >= 0:
        cont += 1
    if numero % 2 == 0:
        pares += (numero,)

print(f'Você digitou os valores {valores}')
print(f'O valor 9 apareceu {valores.count(9)} vezes')
print(f'O valor 3 apareceu na {valores.index(3)+1}ª posição' if 3 in valores else 'O valor 3 não foi digitado em nenhuma posição')
print(f'Os valores pares digitados foram: {pares}' if len(pares) > 0 else 'Nenhum valor par foi digitado')
