import random
from Phrases import frases, phraseses, charm, amuletos

row1 =  ["1🎴 ", "2🎴 ", "3🎴 "]
row2 =  ["4🎴 ", "5🎴 ", "6🎴 "]
row3 =  ["7🎴 ", "8🎴 ", "9🎴 "]
map = [row1, row2, row3]

def destiny(name):
    prhase_number = random.randint(0, 12)            
    message2 = f'\n✨{name}, {phraseses[prhase_number]}✨ \n'
    print(message2)
    charm_number = random.randint(0, 13)
    message3 = f'👉 Your lucky amulet is {charm[charm_number]}\n'
    print(message3)


def choose():
    print("\n 🔮 Welcome to the game of destiny! 🔮 ")
    name = input("\n What is your name? ")
    print("\n You must choose one of the 9 cards below, and if you choose the correct one,")
    print(" you will be able to find a phrase of destiny and a lucky amulet!! 🎁")
    print(f"\n{row1}\n{row2}\n{row3}\n")
    option = int(input("\n Choose a square: "))
    message1 = f" You have choosen the option number {option}..."
    
    if option == 1:
        map[0][0] = "1❎ "      
    elif option == 2:
        map[0][1] = "2❎ "
    elif option == 3:
        map[0][2] = "3❎ "
    elif option == 4:
        map[1][0] = "4❎ "
    elif option == 5:
        map[1][1] = "5❎ "
    elif option == 6:
        map[1][2] = "6❎ "
    elif option == 7:
        map[2][0] = "7❎ "
    elif option == 8:
        map[2][1] = "8❎ "
    elif option == 9:
        map[2][2] = "9❎ "
    else:
        print("\n Please, choice only numbers from 1 to 9\n")

    print(message1)
    print(f"\n{row1}\n{row2}\n{row3}\n")
    input("\n Press Enter to know your fortune...🥁🎵🥁🎶 ").lower()
    destiny(name)

def destino(name):
    prhase_number = random.randint(0, 12)            
    message2 = f'\n✨ {name}, {frases[prhase_number]}✨ \n'
    print(message2)
    charm_number = random.randint(0, 13)
    message3 = f'👉 Tu amuleto de la suerte es {amuletos[charm_number]}\n'
    print(message3)


def elegir():
    print("\n 🔮 ¡Bienvenido al juego del destino! 🔮 ")
    name = input("\n ¿Cuál es tu nombre? ")
    print("\n Debes elegir una de las 9 cartas a continuación,")
    print(" para saber que mensaje tiene la suerte para ti, además de conocer tu amuleto de la suerte!!🎁")
    print(f"\n{row1}\n{row2}\n{row3}\n")
    option = int(input("\n Escoge una carta: "))
    message1 = f" Has elegido la carta número {option}..."
    
    if option == 1:
        map[0][0] = "1❎ "      
    elif option == 2:
        map[0][1] = "2❎ "
    elif option == 3:
        map[0][2] = "3❎ "
    elif option == 4:
        map[1][0] = "4❎ "
    elif option == 5:
        map[1][1] = "5❎ "
    elif option == 6:
        map[1][2] = "6❎ "
    elif option == 7:
        map[2][0] = "7❎ "
    elif option == 8:
        map[2][1] = "8❎ "
    elif option == 9:
        map[2][2] = "9❎ "
    else:
        print("\n Por favor, solo elige número del 1 al 9\n")

    print(message1)
    print(f"\n{row1}\n{row2}\n{row3}\n")
    input("\n Presiona Enter para saber tu fortuna...🥁🎵🥁🎶 ").lower()
    destino(name)


def idioma():
    option = (input("\n 👉 Choose a lenguage: Type 'E' for English or 'S' for Spanish: ").lower())
    if option == "e":
        choose()
    elif option == "s":
        elegir()
idioma()
