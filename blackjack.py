# Importamos módulos
import random, time

# Creamos el deck de cartas
deck = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 10, 'Q': 10, 'K': 10, 'A': 11}

# Definimos función de robar carta
def draw():
    return random.choice(list(deck.keys())) # Convertimos en una lista las claves del diccionario para usar random.choice()

# Definimos la cantidad de jugadores suprimiendo el error de que el usuario meta texto
while True:
    try:
        player_count = int(input("Indica número de jugadores del 1 al 3:"))
        if player_count in [1, 2, 3]:
            break
    except ValueError: # Ignoramos el error de comparar str con int porque es un caso falso
        pass

# Creamos arrays en base a la cantidad de jugadores y añadimos al dealer
all_players = []
dealer = []
all_players.append(dealer)  # Ponemos al dealer en la posición 0, el resto son jugadores
for i in range(player_count):
    player = []
    all_players.append(player)
print(all_players) # DEBUG

# Repartimos primera ronda de cartas
for item in all_players:
    item.append(draw())

# Creamos un array para la suma de valores
counts = []

def recount():
    # Reiniciamos el array de recuento
    counts.clear()

    for player in all_players:
        total = 0
        aces = 0
        for card in player:
            if card == 'A':
                aces += 1
            total += deck[card]
        # Ajustamos el valor de los ases si sobrepasan 21
        while total > 21 and aces:
            total -= 10
            aces -= 1
        counts.append(total)  # Agregamos el total de la mano del jugador a 'counts'
    print(counts)

# Enseñamos las cartas repartidas
out_players = []
while len(out_players) != player_count+1:
    print("length of out_players is:",len(out_players)) #DEBUG
    recount()
    for i, player in enumerate(all_players):
        if i == 0:
            # Toma de decisiones del dealer
            print("La mano del dealer es:")
            for card in player:
                print(card)
            print("El valor de la mano del dealer es:", counts[i])
            if counts[i] <21:
                all_players[i].append(draw())
            else:
                out_players.append(i)
        else:
            if counts[i] > 21:
                print("Te has pasado de 21, OUT")
            else:
                print(f"La mano del Jugador {i} es:")
                for card in player:
                    print(card)
                print(f"\nEl valor de la mano del Jugador {i} es:", counts[i])
                if i not in out_players:
                    while True:
                        respuesta = input("Quieres robar otra carta? (s/n): ").lower()
                        if respuesta in ['s', 'n']:
                            if respuesta == "s":
                                all_players[i].append(draw())
                                print("respuesta s",all_players)
                            else:
                                out_players.append(i)
                            break
                        else:
                            print("Por favor, responde con 's' para sí o 'n' para no.")
                else:
                    print("Has decidido no robar más")
    print("Fin del juego, los resultados son:",counts)
    counts.sort(reverse=True)
    print("Fin del juego, los resultados ORDENADOS son:",counts)
    print(all_players)