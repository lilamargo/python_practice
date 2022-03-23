##______________ Banker Roulette ________________
import random

names_str = input("Give me everybody's names, separated by a comma: ")
names = names_str.split(", ")
num_items = len(names)
x = random.randint(0, num_items -1)
print(names[x])