largura = float(input('Qual a largura da parede em metros?: '))
altura = float(input('Qual a altura da parede em metros?: '))
area = largura * altura
tinta = area / 2
print(f'Você tem {area:.3f} m² de área e precisará de {tinta:.1f} litros de tinta.')
