## 1 year = 365 days
## 1 year = 52 weeks
## 1 year = 12 months

age_input =  input("What is your current age? ")
age = int(age_input)
years =  int(90 - age)
months = int((90 * 12) - (age * 12))
weeks = int((90 * 52) - (age * 12))
days = int((90 * 365) - (age * 365))
message= f"You have {days} days, {weeks} weeks, {months} months, and {years} years left before your 90th birthday..."
print(message)
