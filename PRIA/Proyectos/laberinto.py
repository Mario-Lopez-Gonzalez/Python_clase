import random
import pygame
import time
from collections import deque

class Sign:
    def __init__(self,window_x,window_y):
        self.x = window_x
        self.y = window_y
    
    def draw(self, texto="CHANGE ME", color=(255, 255, 255), fuente_max=100):
        # Configurar Pygame para fuentes
        pygame.font.init()
        
        # Tamaño inicial de la fuente
        tamaño_fuente = fuente_max
        
        # Ajustar el tamaño de la fuente hasta que el texto quepa en la ventana
        fuente = pygame.font.SysFont('Arial', tamaño_fuente)
        while fuente.size(texto)[0] > self.x - 20 or fuente.size(texto)[1] > self.y - 20:
            tamaño_fuente -= 1
            fuente = pygame.font.SysFont('Arial', tamaño_fuente)

        # Crear superficie de texto y rectángulo para centrar
        superficie_texto = fuente.render(texto, True, color)
        rect_texto = superficie_texto.get_rect(center=(self.x // 2, self.y // 2))
        
        # Dibujar el texto centrado en la ventana y rellenar el fondo de negro
        window.fill(black)
        window.blit(superficie_texto, rect_texto)
        pygame.display.update()
        
class Labyrinth:
    def __init__(self, filas=21, columnas=21):
        # Comprobamos que los parámetros sean impares para poder dibujar paredes por el borde, sino sumamos 1
        if filas == 1 or columnas == 1:
            raise Exception("Por favor no introduzcas un 1, que te esperas que se genere?")
        if filas % 2 == 0:
            filas += 1
        if columnas % 2 == 0:
            columnas += 1
        
        # Atributos
        # Tamaños
        self.filas = filas
        self.columnas = columnas
        # El laberinto en sí
        self.lab = [[1 for _ in range(columnas)] for _ in range(filas)]  # Inicializar con paredes        
        # Método para generar el laberinto
        self.crear_laberinto()

    def es_camino(self,x,y):
        # Verifica si la posición (x, y) está dentro de los límites y es un camino
        return 0 <= x < self.filas and 0 <= y < self.columnas and (self.lab[x][y] == 0 or self.lab[x][y] == -2)
    
    def es_pared(self,x,y):
        # Verifica si la posición (x, y) está dentro de los límites y es una pared
        return 0 <= x < self.filas and 0 <= y < self.columnas and self.lab[x][y] == 1
    
    def crear_laberinto(self):
        # Creamos un algoritmo que visite celdas una a una de manera recursiva
        def visitar(x, y):
            # Marcar la celda actual como parte del laberinto
            self.lab[x][y] = 0
            # Direcciones posibles: derecha, abajo, izquierda, arriba
            direcciones = [(0, 2), (2, 0), (0, -2), (-2, 0)]
            random.shuffle(direcciones)  # Mezclar direcciones para aleatoriedad

            # Se intenta caminar
            for dx, dy in direcciones:
                # Desplazamos la coordenada al paso sumando o restando 2
                nx, ny = x + dx, y + dy
                # Verificar si la nueva celda está dentro de los límites y es pared
                if self.es_pared(nx,ny):
                    # Crear un camino entre la celda actual y la nueva celda
                    self.lab[x + dx // 2][y + dy // 2] = 0
                    # Vuelve a ejecutarse a si mismo desde la posición sumada, si no puede deja de avanzar en esa direccion y el bucle continua
                    visitar(nx, ny)

        # Comenzar desde una celda inicial (1, 1)
        visitar(1, 1)
        
        # Crear entrada en la parte superior (0, ?)
        r = random.randint(1,self.columnas-2)
        self.lab[0][r] = -1
        # Creamos atributo con las coordenadas de entrada
        self.entrada = (0,r)
        # Evitamos que el de abajo esté cerrado
        self.lab[1][r] = 0
        # Crear salida en la parte inferior (filas-1, ?)
        r = random.randint(1,self.columnas-2)
        self.lab[self.filas-1][r] = -2
        # Creamos atributo con las coordenadas de salida
        self.salida = (self.filas-1,r)
        # Evitamos que el de encima esté cerrado
        self.lab[self.filas-2][r] = 0

    def draw(self):
        # Borramos todo
        window.fill(black)
        
        # Recorremos las celdas una a una
        for i, fila in enumerate(self.lab):
            for j, celda in enumerate(fila):
                if celda == -1: # Comienzo
                    pygame.draw.rect(window, green, pygame.Rect(
                    i*30, j*30, 30, 30))
                elif celda == -2: # Fin
                    pygame.draw.rect(window, red, pygame.Rect(
                    i*30, j*30, 30, 30))
                elif celda == 0: # Camino
                    pygame.draw.rect(window, white, pygame.Rect(
                    i*30, j*30, 30, 30))

    def draw_steps_dfs(self, pila):
        window.fill(black)
        laberinto.draw()
        for i, j in pila:
            pygame.draw.rect(window, blue, pygame.Rect(
            i*30, j*30, 30, 30))
        pygame.display.update()

    def draw_steps_bfs(self,cola):
        # Limpiamos pantalla solo una vez antes de llamar a la funcion
        for i, j in cola:
            pygame.draw.rect(window, blue, pygame.Rect(
            i*30, j*30, 30, 30))
        pygame.display.update()

    def draw_bfs_path(self,cola):
        for i, j in cola:
            pygame.draw.rect(window, purple, pygame.Rect(
            i*30, j*30, 30, 30))
        pygame.display.update()

    def __str__(self): # Fallback por si falla pygame, para testing con print, pinta rotado 90º
        output = ""
        for fila in self.lab:
            for celda in fila:
                if celda == 1:
                    # Pared en rojo
                    output += "\033[91m#\033[0m "
                else:
                    # Pasillo en blanco
                    output += "  "
            output += "\n"  # Nueva línea al final de la fila
        return output

    def dfs(self):
        # Limpiamos la pantalla una vez dado a que bfs no retrocede
        window.fill(black)
        laberinto.draw()
        pygame.display.update()
        # Movimientos posibles: derecha, abajo, izquierda, arriba
        movimientos = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        # Pila para la ruta y conjunto para las celdas visitadas con la entrada como primer nodo
        pila = [self.entrada]
        visitados = set(pila)
        steps = 0
        # Algoritmo DFS
        while pila:
            # Procesar eventos para evitar que la ventana se congele
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return False

            # Usamos los valores de la parte superior de la pila
            x, y = pila[-1]
            steps += 1
            # Verificar si hemos llegado a la meta
            if (x, y) == self.salida:
                self.draw_steps_dfs(pila)  # Dibujar el camino final
                return steps
            
            # Variable para controlar si encontramos un movimiento válido
            encontrado = False

            # Intentar moverse en las cuatro direcciones
            for dx, dy in movimientos:
                nuevo_x, nuevo_y = x + dx, y + dy
                if self.es_camino(nuevo_x, nuevo_y) and (nuevo_x, nuevo_y) not in visitados:
                    pila.append((nuevo_x, nuevo_y))  # Añadimos a la pila (el camino)
                    visitados.add((nuevo_x, nuevo_y))  # Marcamos la celda como visitada
                    self.draw_steps_dfs(pila)  # Llamamos a dibujar la pantalla
                    encontrado = True
                    time.sleep(0.05)
                    break

            # Si no encontramos un movimiento válido, retrocedemos
            if not encontrado:
                pila.pop()
        
        # Si hemos agotado la pila, no hay solución, esto NO DEBERIA DE OCURRIR
        print("No se encontró una ruta dfs")
        return -1

    def bfs(self):
        #Dibujar el laberinto
        self.draw()
        pygame.display.update()
        # Movimientos posibles: derecha, abajo, izquierda, arriba
        movimientos = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        # Cola para la ruta y conjunto para las celdas visitadas con la entrada como primer nodo
        cola = deque([self.entrada])
        visitados = set([self.entrada])
        
        # Diccionario para rastrear la ruta
        padre = {self.entrada: None}

        # Algoritmo BFS
        while cola:
            # Usamos los valores de la parte frontal de la cola
            x, y = cola.popleft()
            
            # Verificar si hemos llegado a la meta
            if (x, y) == self.salida:
                # Reconstruir la ruta desde el final hasta el comienzo
                camino = []
                while (x, y) is not None:
                    camino.append((x, y))
                    x, y = padre[(x, y)] # TODO bug al llegar aquí
                camino.reverse()  # Invertir para obtener la ruta desde el inicio hasta la salida
                self.draw_bfs_path(camino)
                return len(camino)
            
            # Intentar moverse en las cuatro direcciones
            for dx, dy in movimientos:
                nuevo_x, nuevo_y = x + dx, y + dy
                if self.es_camino(nuevo_x, nuevo_y) and (nuevo_x, nuevo_y) not in visitados:
                    cola.append((nuevo_x, nuevo_y)) # Añadimos a la cola
                    visitados.add((nuevo_x, nuevo_y)) # Añadimos al conjunto de visitados
                    padre[(nuevo_x, nuevo_y)] = (x, y) # Registrar de dónde vino
                    self.draw_steps_bfs(cola)  # Llamamos a dibujar la pantalla
                    time.sleep(0.05)
        # Esto no debería de ocurrir
        print("No se encontró una ruta")
        return None
# Bloque principal

# Invocamos laberinto
x = int(input("Introduce el alto del laberinto:"))
y = int(input("Introduce el ancho del laberinto:"))
laberinto = Labyrinth(x,y)

# Definimos el tamaño de la ventana de pygame según el tamaño del laberinto
window_x = 30 * laberinto.filas
window_y = 30 * laberinto.columnas

# Creamos el cartel
cartel = Sign(window_x,window_y)

# Colores de la pantalla
black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
red = pygame.Color(255, 0, 0)
green = pygame.Color(0, 255, 0)
blue = pygame.Color(0, 0, 255)
purple = (128, 0, 128)

# Iniciamos pygame
pygame.init()

# Abrimos ventana
pygame.display.set_caption('LABERINTO')
window = pygame.display.set_mode((window_x, window_y))

# Llenamos el fondo de la pantalla de negro
window.fill(black)
# Enseñamos el laberinto
laberinto.draw()
pygame.display.update()
time.sleep(1)
# Enseñamos texto
cartel.draw("Método Depth-First Search (DFS)",white)
time.sleep(1.5)
# Comenzamos a contar el tiempo de resolución
inicio = time.perf_counter()
# Resolvemos y guardamos los pasos
steps_dfs = laberinto.dfs()
# Dejamos de contar el tiempo de resolución
fin = time.perf_counter()
# Calculamos la diferencia de tiempos y formateamos para enseñarlo
tiempo = fin - inicio
tiempo_dfs = "{:.4f}".format(tiempo)
text = "Tiempo total: {}s".format(tiempo_dfs)
time.sleep(1)
cartel.draw(text,white)
time.sleep(2)
text = "Total de pasos: {} pasos".format(steps_dfs)
cartel.draw(text,white)
time.sleep(2)
window.fill(black)
laberinto.draw()
pygame.display.flip() # Si el flip se hace en el método da un poco de epilepsia
time.sleep(2)
cartel.draw("Método Breadth-First Search (BFS)",white)
time.sleep(1.5)
# Comenzamos a contar el tiempo de resolución
inicio = time.perf_counter()
# Resolvemos y guardamos los pasos
steps_bfs = laberinto.bfs()
# Dejamos de contar el tiempo de resolución
fin = time.perf_counter()
# Calculamos la diferencia de tiempos y formateamos para enseñarlo
tiempo = fin - inicio
tiempo_bfs = "{:.4f}".format(tiempo)
text = "Tiempo total: {}s".format(tiempo_bfs)
time.sleep(1)
cartel.draw(text,white)
time.sleep(2)
text = "Total de pasos: {} pasos".format(steps_bfs)
cartel.draw(text,white)
time.sleep(2)
window.fill(black)
laberinto.draw()
# Refrescamos la pantalla
pygame.display.update()

# Código para cerrar la ventana con la X
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()

