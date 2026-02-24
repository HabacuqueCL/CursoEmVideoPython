#Faça um programa em python que abra e reproduza o áudio de um arquivo MP3.

import pygame
import sys

pygame.mixer.init()
pygame.mixer.music.load('src\music.mp3')
pygame.mixer.music.set_volume(0.7)
pygame.mixer.music.play(loops=0)

try:
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)
except KeyboardInterrupt:
    pygame.mixer.music.stop()
    sys.exit()

