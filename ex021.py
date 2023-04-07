#Exercício Python 21: Faça um programa em Python que abra e reproduza o áudio de um arquivo MP3.
print('Esse programa só toca uma música!')
import pygame
pygame.init()
pygame.mixer.music.load('ex021.mp3')
pygame.mixer.music.play()
input()
pygame.event.wait()

