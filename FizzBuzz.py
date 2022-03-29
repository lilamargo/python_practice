# You are a going to write a program that automatically prints the soluction to the FizzBuzz game.
# Instructions:
# A: Your program should print each number from 1 to 100 in turn, 
# B: When the number is divisible by 3 then instead of printing the number it should print "Fizz". 
# C: When the number is divisible by 5, then instead of printing the number it should print "Buzz". 
# D: And if the number is divisible by both 3 and 5 e.g. 15, then instead of the number it should print "FizzBuzz". 

#________ Write your solution below: ________

list = []
for number in range(1, 101):
    if number % 3 == 0 and number % 5 == 0:
        list.append("FizzBuzz")
    elif number % 3 == 0:
        list.append("Fizz")
    elif number % 5 == 0:
        list.append("Buzz")
    else:
        list.append(number)
print(list)

#______________Solution 2_____________-
for number in range(1, 101):
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")                        
    else:
        print(number)


