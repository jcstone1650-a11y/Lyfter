##Ejercicio 1
list_of_numbers = list(map(int, input("Ingrese una lista de números separados por espacios: ").split()))
search_number = int(input("Ingrese el número a buscar: "))

count = list_of_numbers.count(search_number)
print(f"El número {search_number} aparece {count} veces en la lista.")


##Ejercicio 2
list_of_numbers = [1, 2, 3, 4, 5, 4, 0, 10, 5, 1, 9, 2]
all_positive = True

for num in list_of_numbers:
    if num <= 0:
        all_positive = False
        break

if all_positive:
    print("La lista no contiene números negativos ni ceros.")
else:
    print("La lista contiene números negativos o ceros.")


##Ejercicio 3
list_of_numbers = [10, 2, 3, 4, 5, 4, 7, 100, 200, 400]
minor = list_of_numbers[0]

for num in list_of_numbers:
    if num < minor:
        minor = num

print(f"El numero menor es: {minor}")


##Ejercicio 4
list_of_numbers = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
average = sum(list_of_numbers) / len(list_of_numbers)
new_list = [x for x in list_of_numbers if x > average]

print(f"Promedio: {average}")
print(f"La nueva lista es: {new_list}")


##Ejercicio 5
words = []

for i in range(5):
    data = input(f"Ingrese la palabra numero {i+1}: ")
    words.append(data)

new_list = [p for p in words if len(p) > 4]

print("Lista original: ", words)
print("Nueva lista: ", new_list)

