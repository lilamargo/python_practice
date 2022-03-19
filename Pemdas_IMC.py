#_________________Operaciones Matemáticas________________________

def operaciones(a, b):
    suma = a + b
    resta = a - b
    multiplicacion = a * b
    division = a / b
    exponencial = a ** b
    multiple_operacion = (a ** b * a / b + a - b)
    multiple_operacion_2 = (a + b - (a ** b))
    
##Nota: Las operaciones multiples se hacen bajo el esquema PEMDAS 
# que significa que se calcularán las operacones de acuerdo a las iniciales de esta palabra, 
# por ejemplo: 
#PEMDAS
# P: Parentesis, 
# E: Exponentes,
# M: Multiplicacion,
# D: Division,
# A: Addition (Suma)
# S: Subtraction (Resta)

    return suma, resta, multiplicacion, division, exponencial, multiple_operacion, multiple_operacion_2
    exit()

#______________________________________Calculo Masa Corporal______________________

def calculo_masa_corporal():
    m = input("Enter your height in m: ")
    kg = input("Enter your weight in kg: ")
    bmi = round(float(kg) / float(m) ** 2, 2)
    if bmi < 18.5:
        print(f"Your BMI is: {bmi} and your weight status is Low")
    elif bmi >= 18.5 and bmi <= 24.9:
        print(f"Your BMI is: {bmi} and your weight status is Normal")
    elif bmi >= 25 and bmi <= 29.9:
        print(f"Your BMI is: {bmi} and your weight status is Overweight")
    else:
        print(f"Your BMI is: {bmi} and your weight status is Obesity")
    
calculo_masa_corporal()



