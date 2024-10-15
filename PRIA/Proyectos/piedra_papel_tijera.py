#Importamos el módulo random
import random

# Marcamos las opciones
choices = ["piedra","papel","tijeras"]

# Inicializamos los contadores
cpu_score = 0
user_score = 0

# Comenzamos bucle de juego
answer = "foo"
while answer != "EXIT":
    # Usamos el paquete random para elegir una de las tres
    cpu_choice = random.choice(choices)

    # Pedimos al usuario su elección
    while True:
        user_choice = input("Elige piedra, papel o tijeras: ")
        if user_choice in choices:
            break

    # Imprimimos las elecciones de ambos
    print("La máquina ha elegido: ",cpu_choice)
    print("Tú has elegido: ",user_choice)

    #Decidimos resultado y sumamos punto
    if cpu_choice == user_choice:
        print("EMPATE")
    elif (cpu_choice == "piedra" and user_choice == "tijeras") or (cpu_choice == "tijeras" and user_choice == "papel") or (cpu_choice == "papel" and user_choice == "piedra"):
        print("HAS PERDIDO")
        cpu_score+=1
    else:
        print("HAS GANADO")
        user_score+=1
    
    # Imprimimos el marcador y le preguntamos al usuario si quiere continuar jugando
    print("El marcador es: usuario->",user_score," y máquina ->",cpu_score)
    answer = input("Para dejar de jugar escribe [EXIT]:")