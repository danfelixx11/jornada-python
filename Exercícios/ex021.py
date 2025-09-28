'''import pygame
pygame.init()
pygame.mixer.music.load('Exercícios/ex021.mp3')
pygame.mixer.music.play()
pygame.event.wait()'''

import pygame, os

print("Diretório atual:", os.getcwd())  # Mostra onde o Python está procurando

pygame.init()
pygame.mixer.music.load(r"D:\Curso Programação\Scripts-python\Exercícios\ex021.mp3")
pygame.mixer.music.play()

while pygame.mixer.music.get_busy():
    pygame.time.Clock().tick(10)
