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
all_players = {'Dealer':0}
name = "foo"
for i in range(player_count):
    name = input(f"Introduce el nombre del jugador {i+1}: ")
    all_players[name] = 0

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

# Comienzo del juego para jugadores
for player in all_players:
    if player == 'Dealer':
        out = False
        score = 0
        hand = []
        hand.append(draw())
        while score < 21 and out != True:
            weight = 1.0
            if score > 17:
                weight = 1 - 0.2*(score-17)
            choice = random.choices(["True","False"],[weight,(1-weight)],k=1) # Elige si seguir robando según el puntuaje, por cada punto por encima de 17 deduce un 20% de probabilidades de robar
            if choice == ['True']: # Se genera como lista el valor lo comparamos directamente con una lista porque honestamente no se que estoy haciendo :)
                hand.append(draw())
            else:
                out = True
            score = add(hand)
        all_players['Dealer'] = score
    else:
        print(f"Turno de {player}")
        time.sleep(1) # Añade 1s de pausa
        score = 0
        out = False
        hand = []
        choice = "foo"
        hand.append(draw())
        score = add(hand)
        print(f"{player}, tu mano es {hand}")
        while score < 21 and out != True:
            print(f"{player}, tienes {score} puntos en tu mano")
            answer = input(f"{player}, quieres robar otra carta?(s/n): ")
            if answer == "s":
                time.sleep(1) # Añadimos pausa 1s
                hand.append(draw())
                score = add(hand)
                print(f"{player}, tu mano es {hand}")
            elif answer == "n": 
                out = True
                all_players[player] = score # Graba los puntos en el listado
            else:
                print("Por favor escribe (s/n)")
        score = add(hand)
        all_players[player] = score
        if score > 21:
            print("Te has pasado de 21")
            time.sleep(2) # Añade 2s de pausa
            all_players[player] = score # Graba los puntos en el listado
        if score == 21:
            print("BLACKJACK!!!!!")
            time.sleep(2) # Añade 2s de pausa
            all_players[player] = score # Graba los puntos en el listado

# Tras que juegen todos los jugadores sacamos al ganador

# Filtramos a los que se han pasado de 21
winners = {}
for player,score in all_players.items():
    if score <= 21:
        winners[player] = score

# Sacamos el valor máximo del puntuaje y creamos un array con los ganadores para saber si hay empate
max_value = max(winners.values())
winner = []
for player,score in winners.items():
    if max_value == score:
        print(f"Added {player} to winners")
        winner.append(player)
        print(f"Winners are {winner}")

# Imprimimos los resultados finales y miramos si hay caso de empate
print(f"El resultado final es de {all_players}")
if len(winner) > 1:
    print(f"Empate, los ganadores son {winner}")
else:
    print(f"El ganador es {winner}")


