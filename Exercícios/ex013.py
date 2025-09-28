salario = float(input("Digite seu salário?: R$ "))
p = float(input('Digite o percentual de aumento recebido?: '))
aumento = (salario / 100) * p
print(f'Seu aumento foi de R$ {aumento:.2f}')
print(f'Seu atual salário saiu de R$ {salario} para R$ {salario + aumento:.2f}')
