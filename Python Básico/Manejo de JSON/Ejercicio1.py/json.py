## Ejercicio 1 
#Investigue cómo leer y escribir archivos JSON en Python aquí.

##Leer
import json

# some JSON:
x = '{"name":"John", "age":30, "city":"New York"}'

# parse x:
y = json.loads(x)

# The result is a python dictionary:
print(y["age"])


##Escribir 
import json

# a Python object (dict):
x = {
    "name": "John",
    "age": 30,
    "city": "New York"
}

# convert into JSON:
y = json.dumps(x)

# the result is a JSON string:
print(y)


## Ejercicio 2 
## Cree un programa que permita agregar un Pokémon nuevo al archivo de la lección de JSON (ipsum:lesson/python-bsico/manejo-de-json)
#Debe leer el archivo para importar los Pokémones existentes.
#Luego debe pedir la información del Pokémon a agregar.
#Finalmente debe guardar el nuevo Pokémon en el archivo.

import json

# Constante para el nombre del archivo
FILENAME = "pokemon.json"

# Leer el archivo de los pokemones
def read_pokemon_file(filename):
    try:
        with open(filename, 'r', encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"Error: El archivo {filename} no existe. Iniciando creación de nueva lista.")
        return []
    except json.JSONDecodeError:
        print(f"Error: El archivo {filename} esta vacio o corrupto. Iniciando creacion de nueva lista.")
        return []

# Solicitar la informacion de los nuevos pokemones
def get_new_pokemon():
    name = input("Nombre del pokemon en (English): ").strip()
    level = int(input("Nivel: ").strip())
    types = input("Tipo(s) separado por coma: ").strip().split(",")
    hp = int(input("HP: ").strip())
    attack = int(input("Attack: ").strip())
    defense = int(input("Defense: ").strip())
    sp_attack = int(input("Sp. Attack: ").strip())
    sp_defense = int(input("Sp. Defense: ").strip())
    speed = int(input("Speed: ").strip())
    
    return {
        "name": {"english": name},
        "level": level,
        "type": [t.strip() for t in types],
        "base": {
            "HP": hp,
            "Attack": attack,
            "Defense": defense,
            "Sp. Attack": sp_attack,
            "Sp. Defense": sp_defense,
            "Speed": speed
        }
    }

# Guardar la informacion de los pokemones
def save_pokemon_file(filename, pokemons):
    try:
        with open(filename, 'w', encoding="utf-8") as f:
            json.dump(pokemons, f, ensure_ascii=False, indent=4)
        print(f"La informacion de los pokemones se guardo con éxito en {filename}.")
    except Exception as e:
        print(f"Error: No se pudo guardar el archivo: {e}.")

# Programa principal
def run_program():
    pokemons = read_pokemon_file(FILENAME)
    new_pokemon = get_new_pokemon()
    pokemons.append(new_pokemon)
    save_pokemon_file(FILENAME, pokemons)

if __name__ == "__main__":
    run_program()