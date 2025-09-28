peso = float(input('Digite seu peso (kg): '))
altura = float(input('Digite sua altura (m): '))
imc = peso / (altura ** 2)
if imc < 18.5:
    print(f'Seu IMC é {imc:.1f}. Você está abaixo do peso ideal.')
    print(f'Seu peso ideal é {18.5 * (altura ** 2):.1f} kg.')
    print(f'Você precisa ganhar {18.5 * (altura ** 2) - peso:.1f} kg para atingir o peso ideal.')
elif 18.5 <= imc < 25:
    print(f'Seu IMC é {imc:.1f}. Você está no peso ideal.')
    print('Parabéns!')
elif 25 <= imc < 30:
    print(f'Seu IMC é {imc:.1f}. Você está acima do peso ideal.')
    print(f'Seu peso ideal é {24.9 * (altura ** 2):.1f} kg.')
    print(f'Você precisa perder {peso - 24.9 * (altura ** 2):.1f} kg para atingir o peso ideal.')
elif 30 <= imc < 40:
    print(f'Seu IMC é {imc:.1f}. Você está com obesidade.')
    print(f'Seu peso ideal é {29.9 * (altura ** 2):.1f} kg.')
    print(f'Você precisa perder {peso - 29.9 * (altura ** 2):.1f} kg para atingir o peso ideal.')
else:
    print(f'Seu IMC é {imc:.1f}. Você está com obesidade mórbida.')
    print(f'Seu peso ideal é {39.9 * (altura ** 2):.1f} kg.')
    print(f'Você precisa perder {peso - 39.9 * (altura ** 2):.1f} kg para atingir o peso ideal.')

# Exercício 043: Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu Índice de Massa Corporal (IMC) e mostre seu status, de acordo com a tabela abaixo:
# - Abaixo de 18.5: Abaixo do Peso
# - Entre 18.5 e 25: Peso Ideal
# - Entre 25 e 30: Acima do Peso
# - Entre 30 e 40: Obesidade
# - Acima de 40: Obesidade Mórbida
