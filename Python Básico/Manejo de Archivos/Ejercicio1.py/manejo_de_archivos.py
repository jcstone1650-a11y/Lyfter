## Ejercicio 1 
# Cree un programa que lea nombres de canciones de un archivo (línea por línea) y guarde en otro archivo los mismos nombres ordenados alfabéticamente.
def read_songs(input_file):
    with open(input_file, 'r', encoding="utf-8") as f:
        songs = [s.strip() for s in f.readlines()]
    return songs 

def sort_list(songs):
    return sorted(songs)

def write_songs(output_file, songs):
    with open(output_file, 'w', encoding="utf-8") as f:
        for s in songs:
            f.write(s + "\n")

def sort_songs():
    try:
        input_file = input("Ingrese el nombre del archivo de entrada: ")
        output_file = input("Ingrese el nombre del archivo de salida: ")
        
        songs = read_songs(input_file)
        sorted_songs = sort_list(songs)
        write_songs(output_file, sorted_songs)
        
        print(f"Las canciones fueron ordenadas y guardadas en {output_file}. ")
    except FileNotFoundError:
        print(f"Error: El archivo {input_file}, no existe. ")
    except Exception as e:
        print("Ocurrio un error: ", e)

if __name__ == "__main__":
    sort_songs()

