# Libreria para limpiar pantalla
import random
import os
os.system("cls")


#Contadores con valores de inicio
victorias_usuario = 0
victorias_computadora = 0
numero_de_rounds = 1

#Opciones
options = ('piedra', 'papel', 'tijeras')

# mensajes de inicio
print("Bienvenid@ al juego ""Piedra, Papel o Tijeras""")
print("El primero que obtenga 3 victorias será el ganador!")
os.system("pause") #Pasa a la siguiente pantalla

# ciclo de juego
while (victorias_usuario < 3) and (victorias_computadora < 3):
    # Pantalla para iniciar cada ronda
    os.system("cls") #limpia la pantalla

    #Muestra el score antes de cada ronda
    print(f"\nLa computadora tiene {victorias_computadora} victorias")
    print(f"Tienes {victorias_usuario} victorias \n")
    print('*'*10)
    print("Round", numero_de_rounds)
    print('*'*10)

    #Eleccion del jugador
    user_plays = input("¿Qué eliges? ").lower()

    #Comprueba que la eleccion del jugador sea válida
    if not user_plays in options:
        print("POR FAVOR ELIGE UNA OPCIÓN VÁLIDA! \n")
        os.system("pause") #Pasa a la siguiente pantalla
        continue

    # La computadora elige despues de validar la eleccion del jugador
    computer_chooses = random.choice(options)
    print(f"La computadora elige: {computer_chooses}")

    # Compara opciones para saber quien gana, pierde o empata
    if computer_chooses == user_plays:
        print("-----> EMPATE! Juguemos de nuevo! \n")
    elif (user_plays == "piedra" and computer_chooses == "tijeras") or (user_plays == "papel" and computer_chooses == "piedra") or (user_plays == "tijeras" and computer_chooses == "papel"):
        victorias_usuario = victorias_usuario + 1
        print("-----> GANASTE! \n")
    elif (user_plays == "piedra" and computer_chooses == "papel") or (user_plays == "papel" and computer_chooses == "tijeras") or (user_plays == "tijeras" and computer_chooses == "piedra"):
        victorias_computadora = victorias_computadora + 1
        print("-----> PERDISTE! \n")
    
    #Actualiza el número de rounds
    numero_de_rounds = numero_de_rounds + 1
    
    #Reinicia el ciclo
    os.system("pause") #Pasa a la siguiente pantalla

# Detiene el juego cuando alguien gana tres veces
    if victorias_computadora == 3:
        os.system("cls") #limpia la pantalla
        print(
            f"La computadora obtuvo {victorias_computadora} victorias \nHAS PERDIDO! jajajaja")
        break
    elif victorias_usuario == 3:
        os.system("cls") #limpia la pantalla
        print(
            f"FELICIDADES!!! Obtuviste {victorias_usuario} victorias \n¡Eres mas listo de lo que pareces!")
        break