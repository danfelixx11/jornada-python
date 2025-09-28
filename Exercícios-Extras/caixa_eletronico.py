print('='*30)
print(f"{'BANCO MENTORIA DEV':^30}")
print('='*30)

valor_saque = int(input('Qual valor você quer sacar? R$ '))

total = valor_saque
cedula_atual = 50 # Começamos com a maior cédula
total_cedulas = 0

while True:
    if total >= cedula_atual:
        # Calcula quantas cédulas do valor autal cabem no total
       total_cedulas = total // cedula_atual
       # Atualiza o total, subtraindo o valor das cédulas entregues
       total = total % cedula_atual
       print(f'Total de {total_cedulas} cédulas de R$ {cedula_atual}')

    # Lógica para passar para a próxima cédula
    if cedula_atual == 50:
        cedula_atual = 20
    elif cedula_atual == 20:
        cedula_atual = 10
    elif cedula_atual == 10:
        cedula_atual = 1

    # Reseta o contador para próxima verificação
    total_cedulas = 0

    # Se o dinheiro acabou, o loop pode parar
    if total == 0:
        break

print('='*30)
print('Volte sempre! Tenha um bom dia!')
