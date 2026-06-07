##Ejercicio 1
#Creamos dos listas con palabras
first_list = ['Hay', 'en', 'que', 'iteracion', 'indices', 'muy']
second_list = ['casos', 'los', 'la', 'por', 'es', 'util']

for i in range(len(first_list)):
    print(first_list[i], second_list[i])


##Ejercicio 2
my_string = 'Pizza con piña'

for i in range(len(my_string)-1, -1, -1):
    print(my_string[i])


##Ejercicio 3
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

my_list[0], my_list[-1] = my_list[-1], my_list[0]
print(my_list)


##Ejercicio 4
new_list = []
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for x in my_list:
    if x % 2 == 0:
        new_list.append(x)

print(new_list)


##Ejercicio 5
numbers = []

for i in range (10):
    number = int(input(f"Ingrese el numero {i+1}: " ))
    numbers.append(number)
print("Los números ingresados son:", numbers)
print("El número mayor es:", max (numbers))
