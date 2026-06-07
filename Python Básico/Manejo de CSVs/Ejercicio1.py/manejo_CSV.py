## Ejercicio 1 
#Cree un programa que me permita ingresar información de n cantidad de videojuegos y los guarde en un archivo csv.

import csv 

#Solicitamos la inforamcion de los videojuegos al usuario
def get_videogame_data():
    name = input("Nombre: ").strip()
    genre = input("Genero: ").strip()
    developer = input("Desarrollador: ").strip()
    rating = input("Clasificacion ESRB: ").strip().upper()
    return {
        'name': name,
        'genre': genre,
        'developer': developer,
        'rating': rating
    }

#Guardamos la informacion en formato CSV
def save_videogames_data_to_csv(filename, videogames):
    try:
        with open(filename, 'w', newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=['name', 'genre', 'developer', 'rating'])
            writer.writeheader()
            writer.writerows(videogames)
        return True
    except Exception as e:
        raise RuntimeError(f"Ocurrio un error a la hora de guardar el archivo CSV: {e}. ")

#Ejecutamos los ejercicios CSV
def run_exercise_videogames():
    try:
        n = int(input("Ingrese la cantidad de videojuegos: "))
        videogames = [get_videogame_data() for _ in range(n)]
        filename = input("Ingrese donde quiere guardar el archivo: ")
        if save_videogames_data_to_csv(filename, videogames):
            print(f"El archivo se creo y se guardo con exito en: {filename}. ")
    except ValueError:
        print(f"Error. Dato erroneo. Intentelo de nuevo. ")
    except Exception as e:
        print(e)

#Codigo principal
def main():
    while True:
        print("\n--- Menu ---")
        print("1. Ingresar y guardar los juegos en CSV")
        print("2. Salir")
        
        choice = input("Ingrese una opcion: ")
        
        if choice == "1":
            run_exercise_videogames()
        elif choice == "2":
            print("Finalizando proceso...")
            break 
        else:
            print("Error: Opcion invalida. Itentelo de nuevo. ")

if __name__ == "__main__":
    main()


## Ejercicio 2
# Lea sobre el resto de métodos del módulo csv aqui y cree una version alternativa del ejercicio de arriba que guarde el archivo separado por tabulaciones en vez de por comas.
import csv 

#Solicitamos la informacion al usuario y lo guardamos en un diccionario
def get_videogames_data():
    name = input('Nombre: ').strip()
    genre = input('Género: ').strip()
    developer = input('Desarrollador: ').strip()
    rating = input('Clasificación ESRB: ').strip().upper()
    return {
        'nombre': name,
        'genero': genre,
        'desarrollador': developer,
        'clasificacion': rating
    }

#Guardar la lista videojuegos (diccionario) en una lista TSV
def save_videogames_to_tsv(filename, videogames):
    try:
        with open(filename, 'w', newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(
                f,
                fieldnames=['nombre', 'genero', 'desarrollador', 'clasificacion'],
                delimiter="\t"
            )
            writer.writeheader()
            writer.writerows(videogames)
        return True
    except Exception as e:
        raise RuntimeError(f"Ocurrio un error guardando el archivo TSV: {e}.")

#Solicitar y ejecutar el archivo CSV
def run_exercise_tsv():
    try:
        n = int(input("Cuantos videojuegos desea ingresar? "))
        videogames = [get_videogames_data() for _ in range(n)]
        filename = input("Ingrese el nombre del archivo TSV de salida: ")
        if save_videogames_to_tsv(filename, videogames):
            print(f"Datos guardados exitosamente en {filename} (formato TSV). ")
    except ValueError:
        print("Error: Debe ingresar un numero valido. ")
    except RuntimeError as e:
        print(e)
        
#Menu principal
def main():
    while True:
        print("\n--- Menu ---")
        print("1. Leer y mostrar los juegos CSV")
        print("2. Salir")
        
        choice = input("Seleccione una opcion: ")
        
        if choice == "1":
            run_exercise_tsv()
        elif choice == "2":
            print("Finalizando proceso...")
            break
        else:
            print("Opcion invalida. Itentelo de nuevo. ")

if __name__ == "__main__":
    main()

