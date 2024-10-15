import random

class Labyrinth:
    def __init__(self, filas=21, columnas=21):
        # Comprobamos que los parámetros sean impares para poder dibujar paredes por el borde
        if filas % 2 == 0 or columnas % 2 == 0:
            raise ValueError("Las dimensiones deben ser impares para permitir paredes.")
        
        # Atributos
        # Tamaños
        self.filas = filas
        self.columnas = columnas
        # El laberinto en sí
        self.lab = [[1 for _ in range(columnas)] for _ in range(filas)]  # Inicializar con paredes
        # Método para generar el laberinto
        self.crear_laberinto()

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
                nx, ny = x + dx, y + dy
                # Verificar si la nueva celda está dentro de los límites
                if 0 <= nx < self.filas and 0 <= ny < self.columnas and self.lab[nx][ny] == 1:
                    # Crear un camino entre la celda actual y la nueva celda
                    self.lab[x + dx // 2][y + dy // 2] = 0
                    visitar(nx, ny)

        # Comenzar desde una celda inicial (1, 1)
        visitar(1, 1)
        
        # Crear entrada en la parte superior (0, ?)
        r = random.randint(1,self.columnas-2)
        self.lab[0][r] = 0
        # Evitamos que el de abajo esté cerrado
        self.lab[1][r] = 0
        # Crear salida en la parte inferior (filas-1, ?)
        r = random.randint(1,self.columnas-2)
        self.lab[self.filas-1][r] = 0
        # Evitamos que el de encima esté cerrado
        self.lab[self.filas-2][r] = 0

    def __str__(self):
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

# Crear un objeto Labyrinth y mostrarlo
x = int(input("Tamaño x del laberinto (impar): "))
y = int(input("Tamaño y del laberinto (impar): "))
laberinto = Labyrinth(x,y)
print(laberinto)

