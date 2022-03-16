def tip_calculator():
    message1 = "Welcome to the tip calculator"
    print(message1)
    bill_str = input("What was the total bill? $")
    bill = float(bill_str)
    percentage_str = input("What percentage tip would you like to give? 10, 12, or 15? ")
    percentage = float(percentage_str)
    
    
    if percentage == 10 or percentage == 12 or percentage == 15:
        people_str = input("How many people to split the bill? ")
        people = int(people_str)
        tip = (bill * (percentage / 100)) + bill
        pay = round(tip / people, 2)
        print(f"Each person should pay: ${pay}")

    else:
        print("The percentage should be only 10, 12 or 15. Please restart the caculator.")     

tip_calculator()