## Ejercicio 1 
##Cree un programa que abra un archivo .csv con la información de videojuegos (el que fue generado en el ejercicio 1) y:
# Lea cada línea usando csv.reader().
# Muestre el contenido en pantalla de forma legible, línea por línea.
import csv

#Leer y convertir las primeras lineas del archivo CSV a una lista de diccionario
def read_videogames_csv(filename):
    try:
        with open(filename, 'r', encoding="utf-8") as f:
            reader = csv.reader(f)
            headers = next(reader)
            rows = [dict(zip(headers, row)) for row in reader]
        return rows 
    except FileNotFoundError:
        raise FileNotFoundError(f"\nError: El archivo {filename} no existe. ")
    except Exception as e:
        raise RuntimeError(f"\nError:Ocurrio un error a la hora de leer el archivo: {e}. ")

#Mostrar los videojuegos en formato legible
def display_videogames(videogames):
    for game in videogames: 
        print(f"Name: {game['name']}")
        print(f"Genre: {game['genre']}")
        print(f"Developer: {game['developer']}")
        print(f"Rating: {game['rating']}")
        print("-" * 40)

#Ejecucion de leer y mostrar contenido del archivo CSV
def run_exercise_read_csv():
    filename = input("Ingrese el nombre del archivo CSV: ")
    try:
        videogames = read_videogames_csv(filename)
        if videogames:
            display_videogames(videogames)
        else:
            print("\nError: El archivo esta vacio o no contiene dato alguno. ")
    except FileNotFoundError as e:
        print(e)
    except RuntimeError as e:
        print(e)

#Menu principal
def main():
    while True:
        print("\n--- Menu ---")
        print("1. Leer y mostrar videojuegos desde CSV")
        print("2. Salir")
        
        choice = input("Seleccione una opcion: ")
        
        if choice == "1":
            run_exercise_read_csv()
        elif choice == "2":
            print(f"Finalizando proceso...")
            break
        else:
            print("\nError: Opcion invalida. Intentelo de nuevo. ")

if __name__ == "__main__":
    main()


## Ejercicio 2 
##Cree un programa que abra un archivo .csv con la información de videojuegos ( en base al CSV que fue generado en el ejercicio 1) y:
# Lea el archivo CSV de videojuegos
# Pida al usuario una clasificación ESRB (por ejemplo: "T")
# Muestre todos los videojuegos que tengan esa clasificación
import csv 

#Leer y guardar la informacion de los videojuegos en una lista de diccionario
def read_videogames(filename):
    try:
        with open(filename, 'r', encoding="utf-8") as f:
            reader = csv.reader(f)
            headers = next(reader)
            rows = [dict(zip(headers, row)) for row in reader]
        return rows
    except FileNotFoundError:
        raise FileNotFoundError(f"\nError: El archivo {filename} no existe. ")
    except Exception as e:
        raise RuntimeError(f"\nError: No se pudo leer el archivo {e}. ")

#Filtrar la informacion por clasificacion ESRB
def filter_by_rating(videogames, esrb_rating):
    return [
        game for game in videogames
        if game['rating'].strip().upper() == esrb_rating.upper()
    ]

#Mostrar la informacion en un formato legible
def display_videogames(videogames, esrb_rating):
    print(f"\nVideojuegos con Clasificacion ESRB {esrb_rating}: ")
    for game in videogames:
        print(f"- {game['name']} (Genre: {game['genre']}, Developer: {game['developer']})")

#Funcion ejecucion por filtro de clasificacion ESRB
def run_exercise_filter_esrb():
    filename = input("Ingrese el archivo ESRB: ")
    esrb_rating = input("Ingrese la clasificacion de los videojuegos (T, M, E): ").strip().upper()
    try:
        videogames = read_videogames(filename)
        filtered = filter_by_rating(videogames, esrb_rating)
        if filtered:
            display_videogames(filtered, esrb_rating)
        else:
            print(f"\nError: El archivo no contiene videojuegos con clasificacion ESRB {esrb_rating}. ")
    except FileNotFoundError as e:
        print(e)
    except RuntimeError as e:
        print(e)

#Menu principal
def main():
    while True:
        print("\n--- Menu ---")
        print("1. Leer videojuegos por filtro de clasificacion ESRB")
        print("2. Salir")
        
        choice = input("Seleccione una opcion: ")
        
        if choice == "1":
            run_exercise_filter_esrb()
        elif choice == "2":
            print(f"Finalizando proceso...")
            break
        else:
            print("\nError: Opcion invalida. Intentelo de nuevo. ")

if __name__ == "__main__":
    main()


## Ejercicio 3 
## Cree un programa que abra un archivo .csv con la información de videojuegos ( en base al CSV que fue generado en el ejercicio 1) y:
#Lea el archivo .csv con videojuegos
#Cuente cuántos videojuegos hay de cada género
#Muestre el resultado de forma ordenada
import csv 
from collections import Counter 

#Leer los videojuegos desde el archivo csv y guardar la informacion en una lista de diccionario 
def read_videogames(filename):
    try:
        with open(filename, 'r', encoding="utf-8") as f:
            reader = csv.reader(f)
            headers = next(reader)
            rows = [dict(zip(headers, row)) for row in reader]
        return rows
    except FileNotFoundError:
        raise FileNotFoundError(f"\nError: El archivo {filename} no existe. ")
    except Exception as e:
        raise RuntimeError(f"\nError: No se pudo leer el archivo: {e}. ")

#Realizar el conteo de genero de los videojuegos
def count_genres(videogames):
    genres = [game['genre'].strip() for game in videogames]
    return Counter(genres)

#Mostrar el conteo de videojuegos por genero
def display_genre_counts(genre_counts):
    print("\nGeneros encontrados: ")
    for genre, count in sorted(genre_counts.items()):
        print(f"{genre}: {count}. ")

#Funcion ejecucion leer y mostrar la informacion en un formato legible 
def run_exercise_count_genres():
    filename = input("Ingrese el archivo CSV: ")
    try:
        videogames = read_videogames(filename)
        if videogames:
            genre_counts = count_genres(videogames)
            display_genre_counts(genre_counts)
        else:
            print("\nError: El archivo esta vacio o no contiene dato alguno. ")
    except FileNotFoundError as e:
        print(e)
    except RuntimeError as e:
        print(e)

#Menu principal
def main():
    while True:
        print("\n--- Menu ---")
        print("1. Contar videojuegos por genero")
        print("2. Salir")
        
        choice = input("Seleccione una opcion: ")
        
        if choice == "1":
            run_exercise_count_genres()
        elif choice == "2":
            print(f"Finalizando proceso...")
            break
        else:
            print("\nError: Opcion invalida. Itentelo de nuevo. ")

if __name__ == "__main__":
    main()


## Ejercicio 4 
## Cree un programa que abra un archivo .csv con la información de videojuegos( en base al CSV que fue generado en el ejercicio 1) y:
#Lea el archivo .csv con videojuegos
#Pida al usuario ingresar el nombre de un desarrollador (ej. "Ubisoft")
#Muestre todos los videojuegos desarrollados por esa empresa en formato legible:
import csv 

#Leer los videojuegos desde un archivo CSV y guardar la informacion en una lista de diccionario
def read_videogames(filename):
    try:
        with open(filename, 'r', encoding="utf-8") as f:
            reader = csv.reader(f)
            headers = next(reader)
            rows = [dict(zip(headers, row)) for row in reader]
        return rows 
    except FileNotFoundError:
        raise FileNotFoundError(f"\nError: El archivo {filename} no existe. ")
    except Exception as e:
        raise RuntimeError(f"\nError: No se puede leer el archivo: {e}. ")

#Filtrar los videojuegos por desallorador
def filter_by_developer(videogames, developer_name):
    return [
        game for game in videogames
        if game['developer'].strip().upper() == developer_name.strip().upper()
    ]

#Mostrar los videojuegos por desarrollador en un formato legible
def display_videogames_by_developer(developer_name, videogames):
    print(f"\nVideojuegos desarrollados por {developer_name}: ")
    for game in videogames:
        print(f"- {game['name']} (Rating: {game['rating']}, Genre: {game['genre']})")

#Funcion ejecucion de filtro de videojuegos por desarrollador
def run_exercise_filter_developer():
    filename = input("Ingrese el archivo CSV: ")
    developer_name = input("Ingrese el nombre del desarrollador: ")
    try:
        videogames = read_videogames(filename)
        filtered = filter_by_developer(videogames, developer_name)
        if filtered:
            display_videogames_by_developer(developer_name, filtered)
        else:
            print(f"\nError: No se encontro ningun videojuego desarrollado por {developer_name}. ")
    except FileNotFoundError as e:
        print(e)
    except RuntimeError as e:
        print(e)

#Menu principal
def main():
    while True:
        print("\n--- Menu ---")
        print("1. Filtrar los videojuegos por desarrollador")
        print("2. Salir")
        
        choice = input("Seleccione un opcion: ")
        
        if choice == "1":
            run_exercise_filter_developer()
        elif choice == "2":
            print(f"Finalizando proceso...")
            break
        else:
            print("\nError: Opcion invalida. Itentelo de nuevo. ")

if __name__ == "__main__":
    main()

