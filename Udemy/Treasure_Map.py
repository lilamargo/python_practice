import random
from Phrases import frases, phraseses, charm, amuletos

row1 =  ["1๐ด ", "2๐ด ", "3๐ด "]
row2 =  ["4๐ด ", "5๐ด ", "6๐ด "]
row3 =  ["7๐ด ", "8๐ด ", "9๐ด "]
map = [row1, row2, row3]

def destiny(name):
    prhase_number = random.randint(0, 12)            
    message2 = f'\nโจ{name}, {phraseses[prhase_number]}โจ \n'
    print(message2)
    charm_number = random.randint(0, 13)
    message3 = f'๐ Your lucky amulet is {charm[charm_number]}\n'
    print(message3)


def choose():
    print("\n ๐ฎ Welcome to the game of destiny! ๐ฎ ")
    name = input("\n What is your name? ")
    print("\n You must choose one of the 9 cards below, and if you choose the correct one,")
    print(" you will be able to find a phrase of destiny and a lucky amulet!! ๐")
    print(f"\n{row1}\n{row2}\n{row3}\n")
    option = int(input("\n Choose a square: "))
    message1 = f" You have choosen the option number {option}..."
    
    if option == 1:
        map[0][0] = "1โ "      
    elif option == 2:
        map[0][1] = "2โ "
    elif option == 3:
        map[0][2] = "3โ "
    elif option == 4:
        map[1][0] = "4โ "
    elif option == 5:
        map[1][1] = "5โ "
    elif option == 6:
        map[1][2] = "6โ "
    elif option == 7:
        map[2][0] = "7โ "
    elif option == 8:
        map[2][1] = "8โ "
    elif option == 9:
        map[2][2] = "9โ "
    else:
        print("\n Please, choice only numbers from 1 to 9\n")

    print(message1)
    print(f"\n{row1}\n{row2}\n{row3}\n")
    input("\n Press Enter to know your fortune...๐ฅ๐ต๐ฅ๐ถ ").lower()
    destiny(name)

def destino(name):
    prhase_number = random.randint(0, 12)            
    message2 = f'\nโจ {name}, {frases[prhase_number]}โจ \n'
    print(message2)
    charm_number = random.randint(0, 13)
    message3 = f'๐ Tu amuleto de la suerte es {amuletos[charm_number]}\n'
    print(message3)


def elegir():
    print("\n ๐ฎ ยกBienvenido al juego del destino! ๐ฎ ")
    name = input("\n ยฟCuรกl es tu nombre? ")
    print("\n Debes elegir una de las 9 cartas a continuaciรณn,")
    print(" para saber que mensaje tiene la suerte para ti, ademรกs de conocer tu amuleto de la suerte!!๐")
    print(f"\n{row1}\n{row2}\n{row3}\n")
    option = int(input("\n Escoge una carta: "))
    message1 = f" Has elegido la carta nรบmero {option}..."
    
    if option == 1:
        map[0][0] = "1โ "      
    elif option == 2:
        map[0][1] = "2โ "
    elif option == 3:
        map[0][2] = "3โ "
    elif option == 4:
        map[1][0] = "4โ "
    elif option == 5:
        map[1][1] = "5โ "
    elif option == 6:
        map[1][2] = "6โ "
    elif option == 7:
        map[2][0] = "7โ "
    elif option == 8:
        map[2][1] = "8โ "
    elif option == 9:
        map[2][2] = "9โ "
    else:
        print("\n Por favor, solo elige nรบmero del 1 al 9\n")

    print(message1)
    print(f"\n{row1}\n{row2}\n{row3}\n")
    input("\n Presiona Enter para saber tu fortuna...๐ฅ๐ต๐ฅ๐ถ ").lower()
    destino(name)


def idioma():
    option = (input("\n ๐ Choose a lenguage: Type 'E' for English or 'S' for Spanish: ").lower())
    if option == "e":
        choose()
    elif option == "s":
        elegir()
idioma()
