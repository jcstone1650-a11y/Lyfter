##Ejercicio 1

#string + string
world1 = "house"
world2 = "Green"
print(world2 + " " + world1)

#string + int
#TypeError: can only concatenate str (not "int") to str
world3 = "black"
number1 = 5
print(world3 + " " + str(number1))

#int + string
#TypeError: unsupported operand type(s) for +: 'int' and 'str'
number2 = 6
world4 = "white"
print(str(number2) + " " + world4)

#list + list
list1 = [1, 2, 3]
list2 = [4, 5, 6]
print(list1 + list2)

#string + list
#TypeError: can only concatenate str (not "list") to str
world5 = "cook"
list3 = ["rice", "beans", "onions"]
print(world5 + " " + str(list3))

#float + int
number3 = 3.19
number4 = 7
print(number3 + number4)

#bool + bool
bool1 = True
bool2 = False
print(bool1 + bool2)


##Ejercicio 2

#Solicitar al usuario que ingrese su nombre, apellido y edad
name = input("¿Cuál es tu nombre?: ")
last_name = input("¿Cuál es tu apellido?: ")
age = int(input("¿Cuál es tu edad?: "))

#Rango de edades
if age <= 2:
    category = "bebé"
elif age <= 9:
    category = "niño"
elif age <= 12:
    category = "preadolescente"
elif age <= 17:
    category = "adolescente"
elif age <= 29:
    category = "adulto joven"
elif age <= 59:
    category = "adulto"
else:
    category = "adulto mayor"

print(f"{name} {last_name}, usted es un {category}.")


##Ejercicio 3

#Juego de adivinar el número secreto entre 1 y 10
import random
secret_number = random.randint(1, 10)

#Bucle para permitir al usuario adivinar hasta que acierte
while True:
    guess = int(input("Adivine el número secreto entre 1 y 10: "))
    if guess == secret_number:
        print("¡Felicidades! Has adivinado el número secreto.")
        break
    elif guess < secret_number:
        print("El número secreto es mayor. Inténtalo de nuevo.")
    else:
        print("El número secreto es menor. Inténtalo de nuevo.")
        

##Ejercicio 4

#Solicitar al usuario que ingrese tres números
num1 = int(input("ingrese el primer número: "))
num2 = int(input("ingrese el segundo número: "))
num3 = int(input("ingrese el tercer número: "))

#Comparar los números para encontrar el mayor
if num1 >= num2 and num1 >= num3:
    mayor = num1
elif num2 >= num1 and num2 >= num3:
    mayor = num2
else:
    mayor = num3

print("El número mayor es:", mayor)


##Ejercicio 5

#Pedir las notas al usuario
total_note = int(input("¿Cúantas notas desea ingresar? "))
notes = []
for i in range(total_note):
    note3 = float(input(f"Ingrese la nota numero {i+1}: "))
    notes.append(note3)
    
#Clasificar aprobadas y desaprobadas
approved = [note3 for note3 in notes if note3 >= 70]
reproved = [note3 for note3 in notes if note3 < 70]

#Calcular cantidades
approved_count = len(approved)
reproved_percentage = len(reproved)

#Calcular promedios
total_average = sum(notes) / len(notes)
average_approved = sum(approved) / len(approved) if approved else 0
average_reproved = sum(reproved) / len(reproved) if reproved else 0

print(f"Cantidad de notas aprobadas: {approved_count}")
print(f"Cantidad de notas desaprobadas: {reproved_percentage}")
print(f"Promedio total: {total_average:.2f}")
print(f"Promedio de notas aprobadas: {average_approved:.2f}")
print(f"Promedio de notas desaprobadas: {average_reproved:.2f}")
