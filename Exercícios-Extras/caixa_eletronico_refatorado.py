print('='*30)
print(f'{'BANCO MENTORIA DEV v2.0':^30}')
print('='*30)

valor_saque = int(input('Qual valor você quer sacar? R$ '))
total_restante = valor_saque

# 1. Criamos uma lista com todas as cédulas disponíveis, da maior para a menor.
cedulas_disponiveis = [50, 20, 10, 1]

#2. O laço 'for' vai passar cada item da nossa lista, um de cada vez.
for cedula in cedulas_disponiveis:

    # 3. Verificamos se o valor restante é suficiente para pelo menos uma cédual do valor atual.
    if total_restante >= cedula:

        # 4. Usamos a divisão inteira (//) para descobrir quantas cédulas cabem.
        quantidade_cedulas = total_restante // cedula

        # 5. Usamos o módulo (%) para descobrir quanto dinheiro sobra depois de entregar as cédulas.
        total_restante = total_restante % cedula

        # 6. Imprimimos o resultado para esta cédula específica.
        print(f'Total de {quantidade_cedulas} cédulas de R$ {cedula}')

print('='*30)
print('Volte sempre! Tenha um bom dia!')
