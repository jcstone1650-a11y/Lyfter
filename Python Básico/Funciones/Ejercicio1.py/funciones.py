## Ejercicio 1
# Cree dos funciones que impriman dos cosas distintas, y haga que la primera llame la segunda.
def greet():
    print("Hola, soy la primera función.")
    farewell()


def farewell():
    print("Adiós, soy la función que se llama al final.")


## Ejercicio 2
# Parte 1
# Intente acceder a una variable definida dentro de una función desde afuera.
def local_example():
    message = "Hola desde dentro de la función"
    print(message)

local_example()

print(message)

# Parte 2
# Intente acceder a una variable global desde una función y cambiar su valor.
count = 0
def increment():
    global count 
    count += 1
    print(f"Contador dentro de la función: {count}")

increment()
print(f"Contador fuera de la función: {count}")


## Ejercicio 3
# Cree una función que retorne la suma de todos los números de una lista.
def sum_list(list):
    sum = 0
    for num in list:
        sum += num
    return sum

numbers = [4, 8, 12, 16]
result = sum_list(numbers)
print(f"La suma es: {result}")


## Ejercicio 4
# Cree una función que le dé la vuelta a un string y lo retorne.
def reverse_string(text):
    return text[::-1]

chain = "Hola mundo"
result = reverse_string(chain)
print(result)


## Ejercicio 5
# Cree una función que cuente cuántas letras mayúsculas y minúsculas hay en un string y lo imprima.
def count_upper_lower(text):
    upper = 0
    lower = 0
    for character in text:
        if character.isupper():
            upper += 1
        elif character.islower():
            lower += 1
    print(f"Hay {upper} mayúsculas y {lower} minusculas.")

chain=("Hola Mundo, La S gano la copa Salchichón.")
result = count_upper_lower(chain)
print(result)


## Ejercicio 6
# Cree una función que acepte un string con palabras separadas por un guion y retorne un string igual pero ordenado alfabéticamente.
def order_words(text):
    word_list = text.split("-")
    word_list.sort()
    result = "-".join(word_list)
    return result 

chain = "python-variable-funcion-computadora-monitor"
final_result = order_words(chain)
print(final_result)


## Ejercicio 7
# Cree una función que acepte una lista de números y retorne una lista con los números primos de la misma.
def is_prime(n):
    if n < 2:   
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def filter_primes(numbers):
    primes = []
    for num in numbers:
        if is_prime(num):
            primes.append(num)
    return primes

nums = [1, 4, 6, 7, 13, 9, 67]
result = filter_primes(nums)
print(result)
