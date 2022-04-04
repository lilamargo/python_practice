## Small Pizza = $15
## Medium Pizza = $20
## Large Pizza = $25
## Pepperoni for Small Pizza = +$2
## Pepperoni for Medium or Large Pizza = +$3
## Extra cheese for any size pizza = + $1
## Tip for Service = +10%
## Promotion Day "2 Large Pizzas" = $45
## Soda any sabor = $2

def orderPizza():
    bill = int(0)
    number = int(input("How many pizzas will you order? "))
    size = str(input(f"What size pizza do you want? S, M or L: "))
    pepperoni = str(input(f"Would you like extra pepperoni? Y or N: "))
    cheese = str(input(f"Would you like extra cheese? Y or N: "))
    soda = str(input(f"Would you like soda? Y or N: "))
    tip = str(input(f"Would you like add tip 10%? Y or N: "))
    if size == "S":
        bill += 15 * number        
        if pepperoni == "Y":
            bill = bill + (2 * number)        
    elif size == "M":
        bill += 20 * number
        if pepperoni == "Y":
            bill = bill + (3 * number)    
    elif size == "L" and number == 1:
        bill += 25
        if pepperoni == "Y":
            bill = bill + (3 * number)    
    elif size == "L" and number == 2:
        bill += 45
        if pepperoni == "Y":
            bill = bill + (3 * number)      
    elif size == "L" and number > 2:
        bill = (((number - 2) * 25) + 45)
        if pepperoni == "Y":
            bill = bill + (3 * number)    
    if cheese == "Y":
        bill = bill + (1 * number)    
    if soda == "Y":
        number_soda = int(input(f"How many sodas?: "))
        if number_soda >= 1:
            bill = bill + (2 * number_soda)    
    if tip == "Y":
        bill = bill + (bill * .10)
    print(f"Your total bill is ${bill}")
    print("Thank you for your order :)")
    
    
orderPizza()