## Cree un programa que abra un archivo .json con la información de Pokémon ( en base al JSON que fue generado en el ejercicio 1) y:
#Lea el archivo JSON de Pokémon
#Recorra la lista de Pokémon y muestre en consola su nombre, tipo y nivel (o cualquier otro atributo definido)

import json

FILENAME = "pokemon.json"

# Leer el archivo JSON y guardar la informacion en la lista de pokemones, mostrar el problema se resolvio de la manera adecuada cuando el archivo no existe o este corrupto
def read_pokemon_file_1(filename):
    try:
        with open(filename, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"Error: El archivo {filename} no existe.")
        return []
    except json.JSONDecodeError:
        print(f"Error: El archivo {filename} no es compatible con JSON.")
        return []

# Mostrar la informacion de los pokemones en un formato legible
def display_pokemons(pokemons):
    if not pokemons:
        print("No hay informacion disponible sobre Pokemones.")
        return

    for pokemon in pokemons:
        name = pokemon["name"]["english"]
        level = pokemon["level"]
        types = ", ".join(pokemon["type"])
        print(f"Name: {name}")
        print(f"Level: {level}")
        print(f"Type(s): {types}")
        print("-" * 40)

# Funcion ejecucion principal: Lee el archivo y muestra los pokemones
def run_exercise_1():  
    pokemons = read_pokemon_file_1(FILENAME)
    display_pokemons(pokemons)

if __name__ == "__main__":
    run_exercise_1()


## Cree un programa que abra un archivo .json con la información de Pokémon ( en base al JSON que fue generado en el ejercicio 1) y:: 
#Lea el archivo JSON de Pokémon
#Pida al usuario un tipo de Pokémon
#Muestre todos los Pokémon que sean de ese tipo

import json

FILENAME = "pokemon.json"

# Leer el archivo JSON y guardar la informacion en la lista de pokemones, mostrar el problema se resolvio de la manera adecuada cuando el archivo no existe o este corrupto
def read_pokemon_file_2(filename):
    try:
        with open(filename, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"Error: El archivo {filename} no existe.")
        return []
    except json.JSONDecodeError:
        print(f"Error: El archivo {filename} no es compatible con JSON.")
        return []

# Filtrar los pokemones por tipo
def filter_pokemons_by_type(pokemons, search_type):
    return [
        pokemon["name"]["english"]
        for pokemon in pokemons
        if any(t.lower() == search_type.lower() for t in pokemon["type"])
    ]

# Funcion ejecucion principal: leer el archivo, preguntar el tipo, mostrar si la informacion coincide
def run_exercise_2():
    pokemons = read_pokemon_file_2(FILENAME)

    if not pokemons:
        print("No Pokémon data available.")
        return

    search_type = input("Ingrese el tipo de Pokémon que desea buscar (agua, electrico, fuego, etc): ").strip()
    results = filter_pokemons_by_type(pokemons, search_type)

    if results:
        print(f"\nLos Pokémon que existen de tipo {search_type} son:")
        for name in results:
            print(name)
    else:
        print(f"No se encontraron Pokémon de tipo '{search_type}'.")

if __name__ == "__main__":
    run_exercise_2()


## Cree un programa que abra un archivo .json con la información de Pokémon ( en base al JSON que fue generado en el ejercicio 1) y:
#Lea el archivo JSON de Pokémon
#Para cada Pokémon, muestre sus estadísticas principales (por ejemplo: ataque, defensa, velocidad, etc.)

import json

FILENAME = "pokemon.json"

# Leer el archivo JSON y guardar la informacion en la lista de pokemones, mostrar el problema se resolvio de la manera adecuada cuando el archivo no existe o este corrupto
def read_pokemon_file_3(filename):
    try:
        with open(filename, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"Error: El archivo {filename} no existe.")
        return []
    except json.JSONDecodeError:
        print(f"Error: El archivo {filename} no es compatible con JSON.")
        return []

# Mostrar las estadisticas principales (ataque, defensa, velocidad) por cada pokemon
def display_pokemon_stats(pokemons):
    if not pokemons:
        print("No hay informacion disponible sobre Pokemones.")
        return

    for pokemon in pokemons:
        name = pokemon["name"]["english"]
        attack = pokemon["base"]["Attack"]
        defense = pokemon["base"]["Defense"]
        speed = pokemon["base"]["Speed"]

        print(f"Nombre: {name}")
        print(f"Ataque: {attack}")
        print(f"Defensa: {defense}")
        print(f"Velocidad: {speed}")
        print("-" * 40)

# Funcion ejecucion principal, leer el archivo y mostrar las estadisticas
def run_exercise_3():
    pokemons = read_pokemon_file_3(FILENAME)
    display_pokemon_stats(pokemons)

if __name__ == "__main__":
    run_exercise_3()


## Cree un programa que abra un archivo .json con la información de Pokémon ( en base al JSON que fue generado en el ejercicio 1) y:
#Lea el archivo JSON
#Agrupe los Pokémon por tipo (por ejemplo, "agua", "fuego", etc.)
#Calcule y muestre el promedio de nivel para cada tipo:

import json
from collections import defaultdict

FILENAME = "Pokemon.json"

# Leer el archivo JSON y mostrar la lista de pokemon
def read_pokemon_file_4(filename):
    try:
        with open(filename, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"Error: El archivo {filename} no existe.")
        return []
    except json.JSONDecodeError:
        print(f"Error: El archivo {filename} no es compatible con JSON.")
        return []

# Ordenar los pokemones por el tipo y calcular el porcentaje de cada tipo
def calculate_average_levels(pokemons):
    type_levels = defaultdict(list)

    for pokemon in pokemons:
        level = pokemon.get("level", 0)
        for t in pokemon.get("type", []):
            type_levels[t].append(level)

    averages = {
        t: sum(levels) / len(levels) if levels else 0
        for t, levels in type_levels.items()
    }
    return averages

# Mostrar el nivel promedio por cada tipo de pokemon
def display_average_levels(averages):
    for t, avg in averages.items():
        print(f"Tipo: {t} → Promedio de nivel: {avg:.1f}")

# Funcion ejecucion principal: leer archivo, calcular promedios y mostrar resultados
def run_exercise_4():
    pokemons = read_pokemon_file_4(FILENAME)
    if not pokemons:
        print("No hay informacion disponible sobre Pokemones.")
        return

    averages = calculate_average_levels(pokemons)
    display_average_levels(averages)

if __name__ == "__main__":
    run_exercise_4()

