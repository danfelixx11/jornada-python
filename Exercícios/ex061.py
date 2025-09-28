primeiro_termo = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão da PA: '))
termo = primeiro_termo
cont = 1
while cont <= 10:
    print(termo, end=' → ')
    termo += razao
    cont += 1
print('FIM')
