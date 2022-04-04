#Love Calculator
# TRUE LOVE

print("\n WELCOME TO THE LOVE CALCULATOR! \n")
name_1 = input("What is your name? \n")
name_2 = input("What is their name? \n")

def true_love():
    name1 = name_1.lower()
    name2 = name_2.lower()
    name = name1 + name2
    t = name.count("t")
    r = name.count("r")
    u = name.count("u")
    e = name.count("e")
    l = name.count("l")
    o = name.count("o")
    v = name.count("v")
    ee = name.count("e")
    truee = t + r + u + e 
    love = l + o + v + ee  
    truee_string = str(truee)
    love_string = str(love)
    union_string = truee_string + love_string
    union_int = int(union_string)
    
    if union_int < 10 or union_int > 90:
        print(f"\n Your score is {union_int}, you go together like coke and mentos \n")
    if (union_int >= 40) and (union_int <= 50):
        print(f"\n Your score is {union_int}, you are alright together \n")
    else:
        print(f"\n Your score is {union_int}, your love is unique \n")

true_love()
