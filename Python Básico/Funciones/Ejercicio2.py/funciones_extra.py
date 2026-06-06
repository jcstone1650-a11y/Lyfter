## Ejercicio 1
# Cree una función que reciba un texto y un carácter, y retorne cuántas veces aparece ese carácter en el texto.
def count_character(text, char):
    count = 0 
    for c in text:
        if c == char:
            count += 1
    return count

first_question = input("Ingrese una palabra o frase: ")
second_question = input("Ingrese el caracter que desea buscar (a, e, i, o, u): ")
word = first_question
character = second_question
result = count_character(word, character)
print(f"La letra '{character}' aparece {result} veces en la frase: {word}. ")


## Ejercicio 2 
# Cree una función que reciba una lista de palabras y un número n, y retorne una nueva lista con solo las palabras que tengan más de n letras.
def filter_words_by_length(words, n):
    result = []
    for word in words:
        if len(word) > n:
            result.append(word)
    return result 

first_question = list(input("Ingrese palabras (separados por espacios): ").split())
second_question = int(input("Ingrese el numero de letras minimas: "))
words_list = first_question
min_length = second_question
final_result = filter_words_by_length(words_list, min_length)
print(f"Las frases que tienen mas de '{min_length}' palabras son: {final_result}. ")


## Ejercicio 3
# Cree una función que reciba un string y retorne cuántas vocales contiene.
def count_vowels(text):
    vowels = "aeiouAEIOU"
    count = 0 
    for char in text:
        if char in vowels:
            count += 1
    return count 

question = input("Ingrese una frase, palabra u oración: ")
phrase = question
result = count_vowels(phrase)
print(f"Hay {result} vocales en la siguiente frase: {phrase}. ")


