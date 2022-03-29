## Aqui podemos ver un ejemplo utilizando el ciclo for con range, 
# donde el 1 es donde inicia el rango y 21 donde finaliza, sin embargo, 
# la cuenta tomará hasta el número 20.
# el número 2 es para indicar de cuanto en cuanto se va a contar.

# for number in range(1, 21, 2):
#     print(number)

# Otro ejemplo que podemos ver es cuando usamos el acumulativo.

# total = 0
# for number in range(1, 101):
#     total += number
# print(total)

# __________Ejercicio:_________
# Sumar solo los numeros impares del 1 al 101
 
suma = 0
for number in range(1, 101, 2):
    suma += number
print(suma)



