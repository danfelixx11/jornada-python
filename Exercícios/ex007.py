n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
media = (n1 + n2) / 2 # Ordem de precedência sempre prioriza os "parenteses primeiro"
print(f'Sua média é: {media:.1f}')
if media >= 7: print("Aprovado!")
