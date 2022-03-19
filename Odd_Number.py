def odd_even():
    print("Is the number odd or even?")
    number = int(input("Which number do you want to choose? "))
    number = number % 2
    if number == 0:
        print("This is an even number")
    else: 
        print("This is an odd number")

odd_even()