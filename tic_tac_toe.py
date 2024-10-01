import pygame

# Tamaño de la ventana emergente
window_x = 720
window_y = 480

# Colores del juego
black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
red = pygame.Color(255, 0, 0)
blue = pygame.Color(0, 0, 255)

# Iniciamos pygame
pygame.init()

# Abrimos ventana
pygame.display.set_caption('TIC-TAC-TOE')
game_window = pygame.display.set_mode((window_x, window_y))

