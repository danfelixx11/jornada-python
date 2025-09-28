#IMPORTAÇÃO COMPLETA DA BIBLIOTECA MATH
'''import math
angulo = float(input('Digite o ângulo que você deseja: '))
seno = math.sin(math.radians(angulo))
print(f'O ângulo de {angulo} de seno de {seno:.2f} ')
cosseno = math.cos(math.radians(angulo))
print(f'O ângulo de {angulo} tem o cosseno de {cosseno:.2f}')
tangente = math.tan(math.radians(angulo))
print(f'O ângulo de {angulo} tem a tangente de {tangente:.2f}')'''

#IMPORTAÇÃO APENAS DAS REFERENCIAS USADAS NO CÓDIGO
from math import radians, sin, cos, tan
angulo = float(input('Digite o ângulo que você deseja: '))
seno = sin(radians(angulo))
print(f'O ângulo de {angulo} de seno de {seno:.2f} ')
cosseno = cos(radians(angulo))
print(f'O ângulo de {angulo} tem o cosseno de {cosseno:.2f}')
tangente = tan(radians(angulo))
print(f'O ângulo de {angulo} tem a tangente de {tangente:.2f}')
