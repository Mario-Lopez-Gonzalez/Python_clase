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
all_players = {'name':'Dealer', 'score':0}
name = "foo"
for i in range(player_count):
    name = input(f"Introduce el nombre del jugador {i+1}: ")
    all_players[name] = 0
print(all_players)
# Función de sumatorio del valor de una mano
def add(hand):
    total = 0
    aces = 0
    for card in hand:
        if card == 'A':
                aces += 1
        total += deck[card]
    while total > 21 and aces:
        total -= 10
        aces -= 1
    return total
total_scores = {}

# Comienzo del juego para jugadores
for player in all_players:
    score = 0
    out = False
    hand = []
    choice = "foo"
    hand.append(draw())
    score = add(hand)
    print("Tu mano es",hand)
    while score < 21 and out != True:
        print(f"Tienes {score} puntos en tu mano")
        answer = input("Quieres robar otra carta?(s/n): ")
        if answer == "s":
           hand.append(draw())
           score = add(hand)
           print("Tu mano es",hand)
        elif answer == "n": 
            out = True
        else:
            print("Por favor escribe (s/n)")
    score = add(hand)
    all_players[player] = score
    if score > 21:
        print("Te has pasado de 21")
    print("Turno del siguiente jugador")

# Comienzo del juego para la CPU
score = 0
hand = []
hand.append(draw())
while score < 21:
    hand.append(draw())
    score = add(hand)
all_players['Dealer'] = score

print(total_scores)

