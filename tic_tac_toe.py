import pygame
import random

# Tamaño de la ventana emergente
window_x = 600
window_y = 600

# Tamaño de celda
grid = window_x//3

# Colores del juego
black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
red = pygame.Color(255, 0, 0)
blue = pygame.Color(0, 0, 255)

# Creamos tablero
board = [[0,0,0]
        ,[0,0,0]
        ,[0,0,0]]

# Flag de si se ha intentado el primer turno de la CPU
cpu_start = False

# Iniciamos pygame
pygame.init()

# Abrimos ventana
pygame.display.set_caption('TIC-TAC-TOE')
game_window = pygame.display.set_mode((window_x, window_y)) #

# Elegimos fuente para el texto
font = pygame.font.Font(None, 250)

def draw(symbol,x,y):
    if symbol == "x":
        # Renderizar el texto (crear una superficie con el texto)
        text_surf = font.render("X", True, red)

        # Obtener el rectángulo del texto para centrarlo o moverlo
        text_rect = text_surf.get_rect()
        text_rect.center = (x,y)  # Mover a ubicación para test a 1,1

        # Dibujar el texto en la pantalla
        game_window.blit(text_surf, text_rect)
    else:
        # Renderizar el texto (crear una superficie con el texto)
        text_surf = font.render("O", True, blue)

        # Obtener el rectángulo del texto para centrarlo o moverlo
        text_rect = text_surf.get_rect()
        text_rect.center = (x,y)  # Mover a ubicación para test a 1,1

        # Dibujar el texto en la pantalla
        game_window.blit(text_surf, text_rect)

def cpu():
    x = random.randint(0,600)
    y = random.randint(0,600)
    # Normalizamos las coordenadas al centro del cuadrante más cercano
    x_n = x // 200
    y_n = y // 200
    while board[x_n][y_n] != 0: # Si esta cogido vuelve a sacar número
        x = random.randint(0,600)
        y = random.randint(0,600)
        x_n = x // 200
        y_n = y // 200
    board[x_n][y_n] = "o"
    x = ((x_n))*200 + 200/2
    y = ((y_n))*200 + 200/2
    draw("o",x,y)

def check_win():
    
    # Mirar filas
    for x,col in enumerate(board):
        if col[0] == col[1] == col[2] and col[0] != 0:
            return ["col",col[0],[(x,0),(x,1),(x,2),]]  # Devuelve condicion de victoria, simbolo ganador y que fila
    
    # Mirar columnas
    for row in range(3):
        if board[0][row] == board[1][row] == board[2][row] and board[0][row] != 0:
            return ["row",board[0][row],[(0,row),(1,row),(2,row)]] # Devuelve condicion de victoria, simbolo ganador y que columna
    
    # Verificar diagonal principal
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != 0:
        return ["diag",board[0][0],[(0,0),(1,1),(2,2)]]  # Devuelve condicion de victoria, simbolo ganador y que diagonal

    # Verificar diagonal secundaria
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != 0:
        return ["diag",board[0][2],[(0,2),(1,1),(2,0)]]
    return None
# Funcion principal
while True:

# Dibujar las líneas verticales
    for i in range(1, 3):
        pygame.draw.line(game_window, white, (i * grid, 0), (i * grid, window_y), 2)

    # Dibujar las líneas horizontales
    for i in range(1, 3):
        pygame.draw.line(game_window, white, (0, i * grid), (window_x, i * grid), 2)

    # Actualizar la pantalla
    pygame.display.flip()

    if random.choice([1,2]) == 2 and not cpu_start: # Comienza CPU
        cpu()
        cpu_start = True
    else: # No comienza cpu pero se ha intentado (se evita que rollee cada frame para ganar)
        cpu_start = True

    # Manejo de teclas
    for event in pygame.event.get(): # Le pedimos a pygame que nos devuelva los eventos    
        if event.type == pygame.MOUSEBUTTONDOWN: # Hacer click izquierdo
            # Obtener coordenadas del clic
            x , y = pygame.mouse.get_pos()
            # Sacamos el cuadrante correspondiente
            x_n = x // 200
            y_n = y // 200
            if board[x_n][y_n] == 0: # Click en celda libre
                # Actualizamos el estado del tablero
                board[x_n][y_n] = "x"
                # Normalizamos las coordenadas al centro del cuadrante más cercano
                x = ((x_n))*200 + 200/2
                y = ((y_n))*200 + 200/2
                draw("x",x,y)
                if sum(row.count(0) for row in board) == 0 or check_win(): #No hay huecos
                    print(check_win())
                    pygame.quit()
                    quit()
                cpu() # Turno de la CPU
                if sum(row.count(0) for row in board) == 0 or check_win(): #No hay huecos
                    print(check_win())
                    pygame.quit()
                    quit()
        if event.type == pygame.KEYDOWN: # Escape del juego up arrow
            if event.key == pygame.K_UP: 
                pygame.quit()
                quit()

