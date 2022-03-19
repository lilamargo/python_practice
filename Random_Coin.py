import random 

random_integer = random.randint(1, 10)
print(random_integer)

# El Random de tipo random, considera los números del 0.000... al 0.999...
random_float = random.random()

# Pero si quiero que considere hasta cierto número, lo multiplico por este. Por ejemplo, por 5 me llegarán
# de 0.0000... hasta 4.9999
random_float *= 5
print(random_float)

# ____________ Game Heads or Tails______________

def cara_cruz():
    random_coin = random.randint(0, 1)
    if random_coin == 0:
        print("\nHead!!\n")
    else:
        print("\nTrain!!\n")

def start():
    print("\nFlip the coin and you will know your luck with Heads or Tails\n")
    option = (input("\n Press Enter to continue... ").lower())
    cara_cruz()
start()