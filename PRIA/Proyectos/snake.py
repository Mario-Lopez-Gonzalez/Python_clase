import pygame
import random
import time
import os
import sys

# Velocidad inicial de la serpiente
snake_speed = 15

# Tamaño de la ventana emergente
window_x = 720
window_y = 480

# Colores del juego
black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
red = pygame.Color(255, 0, 0)
green = pygame.Color(0, 255, 0)
blue = pygame.Color(0, 0, 255)

# Iniciamos pygame
pygame.init()

# Abrimos ventana
pygame.display.set_caption('SNAKE')
game_window = pygame.display.set_mode((window_x, window_y))

# Controlador de fotogramas por segundo
fps = pygame.time.Clock()

# Spawnpoint de la serpiente y contador de la posición de la cabeza
snake_position = [100, 50]

# Definimos las coordenadas de los primeros 4 segmentos de la serpiente
# body
snake_body = [  [100, 50], #Coincide con snake_position y nos va a marcar el punto central del personaje
                [90, 50],
                [80, 50],
                [70, 50]
            ]
# Cálculo de la posición de la fruta y si aparece en pantalla
fruit_position = [[random.randrange(1, (window_x//10)) * 10,
                  random.randrange(1, (window_y//10)) * 10]]
fruit_spawn = True

fruit_uneaten = 0 # Creamos una variable que cree más frutas si el jugador no ha comido una fruta en un tiempo

fruit_eaten = False # Control para saber si nos hemos comido una fruta este frame

# Creamos la dirección de la serpiente y le damos una de comienzo
direction = 'RIGHT'
change_to = direction

# Puntos iniciales
score = 0

# Función para enseñar los puntos
def show_score(choice, color, font, size):
  
    # Creamos objeto fuente del puntuaje
    score_font = pygame.font.SysFont(font, size)
    
    # Creamos el fondo del puntuaje con render
    score_surface = score_font.render('Puntos : ' + str(score), True, color)
    
    # Creamos un rectangulo para el puntuaje
    score_rect = score_surface.get_rect()
    
    # Sacamos el texto en la ventana superponiendo el fondo creado en el rectangulo designado
    game_window.blit(score_surface, score_rect)

# Definimos el game over
def game_over():
  
    # Creamos el objeto fuente
    my_font = pygame.font.SysFont('times new roman', 20)
    
    # Creamos el fondo del texto
    game_over_surface = my_font.render('GAME OVER: ' + str(score)+' Continuar?(Click Izquierdo Sí, Click Derecho No)', True, red)
    
    # Creamos el rectangulo del fondo
    game_over_rect = game_over_surface.get_rect()
    
    # Coordenadas del texto (en el medio)
    game_over_rect.midtop = (window_x/2, window_y/4)
    
    # Escribimos el texto con blit
    game_window.blit(game_over_surface, game_over_rect)
    pygame.display.flip()
    
    # Preparamos opciones para continuar jugando
    while True:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    os.execl(sys.executable, sys.executable, *sys.argv)
                if event.button == 3:           
                    time.sleep(2)
                    pygame.quit()
                    quit()

# Funcion principal
while True:
  
    # Manejo de teclas
    for event in pygame.event.get(): # Le pedimos a pygame que nos devuelva los eventos
        if event.type == pygame.KEYDOWN: # Nos enfocamos en las teclas pulsadas
            if event.key == pygame.K_UP or event.key == ord('w'): # Verificamos que tecla está siendo pulsada
                change_to = 'UP' # Cambiamos la dirección de la serpiente a la pulsada en el siguiente frame
            if event.key == pygame.K_DOWN or event.key == ord('s'):
                change_to = 'DOWN'
            if event.key == pygame.K_LEFT or event.key == ord('a'): # Implementamos control por WASD
                change_to = 'LEFT'
            if event.key == pygame.K_RIGHT or event.key == ord('d'):
                change_to = 'RIGHT'

    # Bloqueamos movimientos contrarios de teclas priorizando la primera
    if change_to == 'UP' and direction != 'DOWN':
        direction = 'UP'
    if change_to == 'DOWN' and direction != 'UP':
        direction = 'DOWN'
    if change_to == 'LEFT' and direction != 'RIGHT':
        direction = 'LEFT'
    if change_to == 'RIGHT' and direction != 'LEFT':
        direction = 'RIGHT'

    # Modificamos las posiciones según la tecla pulsada
    if direction == 'UP':
        snake_position[1] -= 10
    if direction == 'DOWN':
        snake_position[1] += 10
    if direction == 'LEFT':
        snake_position[0] -= 10
    if direction == 'RIGHT':
        snake_position[0] += 10

    snake_body.insert(0, list(snake_position)) # Creamos nuevo bloque en la misma posición que estamos y lo colocamos como cabeza
    # Que hacemos cuando la serpiente se come la fruta
    for fruit in fruit_position:
        if snake_position[0] == fruit[0] and snake_position[1] == fruit[1]: # Comparamos las coordenadas x e y del jugador y la fruta
            score += 10 # Sumamos puntos
            fruit_position.remove(fruit) # Quitamos la fruta de la lista
            fruit_spawn = False # Avisamos que no hay fruta
            snake_speed+=1 # Aceleramos un poco el juego por cada fruta consumida
            fruit_eaten = True
            break

    if not fruit_eaten:
        snake_body.pop() # Borramos el camino anterior de la serpiente para animar que avanza
    fruit_eaten = False

    fruit_uneaten += 1 # Sumamos 1 al contador de fruta sin comer

    if not fruit_spawn or fruit_uneaten > 100: # Si avisamos que no hay fruta o el contador llega a 100 spawneamos otra
        fruit_position.append([random.randrange(1, (window_x//10)) * 10, 
                          random.randrange(1, (window_y//10)) * 10])
        fruit_uneaten = 0
        
    fruit_spawn = True # Reactivamos el flag de la fruta para no crear duplicadas
    game_window.fill(black) # Llenamos el fondo de la pantalla de negro
    
    for pos in snake_body: # Por cada segmento de la serpiente
        if score < 100:
            pygame.draw.rect(game_window, green, pygame.Rect(
              pos[0], pos[1], 10, 10)) # Dibujamos un rectangulo en la ventada de juego, de color verde,
                                   # en la posición x e y y de 10x10 pixeles
        else: # Si tenemos 100 puntos o mas vuelve a la serpiente multicolor
            pygame.draw.rect(game_window, pygame.Color(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)),pygame.Rect(
              pos[0], pos[1], 10, 10))
    
        for pos in fruit_position:    
            pygame.draw.rect(game_window, white, pygame.Rect( # Dibujamos la fruta con la misma logica
            pos[0], pos[1], 10, 10))

    # Condiciones del game over
    if snake_position[0] < 0 or snake_position[0] > window_x-10: # Comprobamos si estamos tocando la pantalla en los ejes x e y
        game_over()
    if snake_position[1] < 0 or snake_position[1] > window_y-10:
        game_over()
    
    # Comprobamos si estamos tocando algun segmento de la serpiente con la cabeza
    for block in snake_body[1:]: # Empezamos desde el segundo bloque porque el primero es la cabeza, aunque realisticamente es imposible que el primer bloque toque algo que no sea un bloque a partir del 5to
        if snake_position[0] == block[0] and snake_position[1] == block[1]: # Comparamos coordenadas
            game_over()
    
    # Dibujamos el puntuaje cada frame
    show_score(1, white, 'times new roman', 20)
    
    # Refrescamos la pantalla
    pygame.display.update()

    # FPS y tasa de refresco, lo cual corresponde con la velocidad del juego
    fps.tick(snake_speed)
