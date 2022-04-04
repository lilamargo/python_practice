# Treasure Island

def treasure_island():
    print("\n Welcome to Trausure Island. Your mission is to find the treasure. \n")
    name = (input("What is your pirate name? "))
    left_right = (input(f'You are at a cross road. Where do you want to go? Type "left" or "right":  \n').lower())
    if left_right == "right":
        print(f"\n Game Over. {name}, you have fallen into a bear trap!\n")
    elif left_right == "left":
        swim_wait = (input(f'You come to a lake. There is an island in the middle of the lake. Type "Wait" to wait for a boat. Type "Swim" to swim across:  \n').lower())
        if swim_wait == "swim":
            print(f"\n Game Over. {name}, a piranha has attacked you.\n")
        elif swim_wait == "wait":
            red_blue = (input(f'You arrive at the island unharmed. There is a house with 3 doors. One "Red", One "Yellow" and one "Blue". Which colour do you choose? Type de colour: \n'))
            if red_blue == "red":
                print(f"\n Game Over. {name}, a zombie has come out of the red door, it has infected you with the T virus.\n")
            elif red_blue == "blue":
                print(f"\n Game Over. {name}, after continuing through the blue door, you walked down a long path and realized that it led you to the beginning of everything.\n")
            elif red_blue == "yellow":
                print(f"\n Opening the yellow door, everything was dark...\n while walking without being able to see anything, then, a small light appeared and you go to it. \n The light was golden and flickering. Upon reaching it you realized that it was a beautiful gold box,\n you touched it and a melodious voice appeared: '{name}, you have found the treasure of destiny, you deserve the jewel that contains it'...\n")  

def isla_tesoro():
    print("\n Bienvenido(a) a la isla del tesoro. Tu misión es encontrar el tesoro. \n")
    name = (input("¿Cuál es tu nombre pirata? "))
    left_right = (input(f'Estás en una encrucijada. ¿A donde quieres ir? Escriba "izquierda" o "derecha":  \n').lower())
    if left_right == "derecha":
        print(f"\n Juego terminado. {name}, has caído en una trampa para osos!\n")
    elif left_right == "izquierda":
        swim_wait = (input(f'Llegas a un lago. Hay una isla en medio del lago. Escribe "Esperar" para esperar un barco. Escribe "Nadar" para cruzar a nado:  \n').lower())
        if swim_wait == "nadar":
            print(f"\n Juego terminado. {name}, una piraña te ha atacado.\n")
        elif swim_wait == "esperar":
            red_blue = (input(f'Llegas a la isla ileso. Hay una casa con 3 puertas. Una "Roja", una "Amarilla" y otra "Azul". ¿Qué color eliges?: \n'))
            if red_blue == "roja" or red_blue == "rojo":
                print(f"\n Juego terminado. {name}, un zombi ha salido por la puerta roja, te ha infectado con el virus T.\n")
            elif red_blue == "azul":
                print(f"\n Juego terminado. {name}, después de continuar a través de la puerta azul, caminaste por un largo camino y te diste cuenta de que te llevaba al principio de todo..\n")
            elif red_blue == "amarillo" or red_blue == "amarilla":
                print(f"\n Al abrir la puerta amarilla, todo estaba oscuro...\n mientras caminabas sin poder ver nada, entonces, apareció una pequeña luz y te acercaste a ella. \n La luz era dorada y parpadeante. Al llegar a ella te diste cuenta que era una hermosa caja de oro,\n la tocaste y apareció una melodiosa voz: '{name}, has encontrado el tesoro del destino, te mereces la joya que lo contiene'...\n")  


def idioma():
    option = (input("Choose a lenguage: Type 'E' for English or 'S' for Spanish: ").lower())
    if option == "e":
        treasure_island()
    elif option == "s":
        isla_tesoro()
idioma()



