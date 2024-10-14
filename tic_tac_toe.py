import pygame # type: ignore
import random
import time

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
green = pygame.Color(0, 255, 0)

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
font2 = pygame.font.Font(None,200)

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
     # Simulamos si podemos ganar recorriendo el array uno a uno y poniendo "o" en las vacías
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == 0: # Si la casilla esta vacía...
                board[i][j] = "o" # Simulamos un movimiento
                if check_win(): # Si ganamos con ese movimiento lo dejamos y dibujamos
                    draw("o",i * 200 + 200/2 ,j * 200 + 200/2) # Forzamos dibujo al centro del grid
                    return None # Es literalmente un break
                else:
                    board[i][j] = 0 # Si no ganamos deshacemos y dejamos como estaba

    # Simulamos si puede ganar el jugador con el mismo método
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == 0:
                board[i][j] = "x" # Simulamos un movimiento pero con "x"
                if check_win(): # Miramos si ganaría el humano
                    board[i][j] = "o" # Borramos la X simulada por nuestra O o sino fallaría la lógica de todo
                    draw("o",i * 200 + 200/2 ,j * 200 + 200/2)
                    return None # Es literalmente un break
                else:
                    board[i][j] = 0 # Si no ganamos deshacemos y dejamos como estaba

    # Esto solo corre si hay que jugar de forma aleatoria porque no hay movimientos ganadores
    # Escogemos coordenadas aleatorias
    x = random.randint(0,600)
    y = random.randint(0,600)
    # Normalizamos las coordenadas al centro del cuadrante más cercano
    x_n = x // 200
    y_n = y // 200
    while board[x_n][y_n] != 0: # Si está cogido vuelve a sacar número y normalizamos
        x = random.randint(0,600)
        y = random.randint(0,600)
        x_n = x // 200
        y_n = y // 200
    board[x_n][y_n] = "o" # Colocamos la ficha y calculamos coordenadas para dibujar
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
        return ["diag",board[0][2],[(0,2),(1,1),(2,0)]] # Devuelve condicion de victoria, simbolo ganador y que diagonal
    return None

def end(cond,winner,pos_arr): # recibe condicion de victoria, ganador y un array con las celdas a dibujar
    # Calculamos el comienzo y fin de la linea ganadora
    start_pos = (pos_arr[0][0] * 200 + 200 // 2, pos_arr[0][1] * 200 + 200 // 2) # pos_arr es lista de tuplas por tanto pos_arr[0] == primera tupla y pos_arr[0][0] es x de la primera tupla
    end_pos = (pos_arr[2][0] * 200 + 200 // 2, pos_arr[2][1] * 200 + 200 // 2)  # (x, y)
    for i in range(30): # Creamos un refresco de 30 veces con colores aleatorios para efector arcoiris
        pygame.draw.line(game_window, pygame.Color(random.randint(0,255), random.randint(0,255), random.randint(0,255)), start_pos, end_pos, 10)
        pygame.display.flip()
        time.sleep(0.1)
    pygame.quit()
    quit()

def end_draw():
    # Creamos texto con font2 para que quepa en pantalla (es de 200 en vez de 250 pixeles)
    text_surf = font2.render("EMPATE", True, white)
    text_rect = text_surf.get_rect()
    text_rect.center = (300,300)
    game_window.blit(text_surf, text_rect)
    pygame.display.flip() # Creo que no hace nada
    time.sleep(2)
    pygame.quit()
    quit()

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

    # Determinamos si comienza la CPU
    if random.choice([1,2]) == 2 and not cpu_start: 
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
                # Normalizamos las coordenadas al centro del cuadrante más cercano y dibujamos
                x = ((x_n))*200 + 200/2
                y = ((y_n))*200 + 200/2
                draw("x",x,y)
                #Miramos si el humano gana o si no hay mas celdas
                if check_win():
                    end(*check_win())
                elif sum(row.count(0) for row in board) == 0: # No hay celdas
                    end_draw()
                # Turno de la CPU
                cpu()
                # Miramos si la CPU ha ganado o si no hay más espacios libres, sino se repite el bucle principal y le toca al humano
                if check_win():
                    end(*check_win())
                elif sum(row.count(0) for row in board) == 0: # No hay celdas
                    end_draw() 

# TODO meter música resultados WIN/LOSE/DRAW (?)