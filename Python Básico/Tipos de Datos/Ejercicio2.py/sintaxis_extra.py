##Ejercicio 1
#Haga uso de la variable try y except para manejar errores en caso de que el usuario ingrese un valor no numérico o un número negativo o cero.
try:
    price = float(input("Ingrese el precio del producto: "))
    if price <= 0:
        print("Error: El precio debe ser un número positivo o mayor a 0")
    elif price < 100:
        discount = price * 0.02
        final_price = price - discount
        print(f"Tienes un descuento del 2%, el precio final es: {final_price}")
    else:  
        discount = price * 0.10
        final_price = price - discount
        print(f"Tienes un descuento del 10%, el precio final es: {final_price}")
except ValueError:
    print("Error: Debe ingresar un número válido, no letras ni simbolos. ")


##Ejercicio 2
seconds = int(input("Ingrese el tiempo en segundos: "))
if seconds <= 0:
        print("Error: El tiempo debe ser un número positivo o mayor a 0")
elif seconds > 600:
        print("El tiempo es mayor a 10 minutos.")
elif seconds < 600:
        remainig_seconds = 600 - seconds
        print(f"El tiempo es menor a 10 minutos. Le faltan {remainig_seconds} segundos para llegar a 10 minutos.")
else:  
        print("El tiempo es exactamente 10 minutos.")


##Ejercicio 3
n = int(input("Ingrese un numero: "))
total_sum = n * (n + 1) // 2
print(f"La suma de los números del 1 al {n} es {total_sum}")


##Ejercicio 4
import random
secret_number = random.randint(1, 10)

bucle = True
while bucle:
    number = int(input("Ingrese un número entre 1 y 10: "))
    if number < 1 or number > 10:
        print("Error: Solo se permiten numeros entre el 1 y el 10.")
    elif number == secret_number:
        print("Felicidades!: Has adivinado el número secreto.") 
        bucle = False
    else:
        print("Número incorrecto. Intentelo de nuevo.")


##Ejercicio 5
num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))
num3 = int(input("Ingrese el tercer número: "))

if num1 == 30 or num2 == 30 or num3 == 30 or (num1 + num2 + num3) == 30:
    print("Correcto")
else:
    print("Incorrecto")


##Ejercicio 6
celsius = float(input("Ingrese la temperatura en grados Celsius: "))
fahrenheit = (celsius * 9/5) + 32
kelvin = celsius + 273.15

print(f"Celsius: , {celsius}")
print(f"Fahrenheit: , {fahrenheit}")
print(f"Kelvin: , {kelvin}")


##Ejercicio 7
number = int(input("Ingrese un número del 1 al 10: "))

if 1 <= number <= 10:
    for i in range(1, 13):
        result = number * i
        print(f"{number} x {i} = {result}")
else:
    print("Error: El número debe estar entre 1 y 10.")

