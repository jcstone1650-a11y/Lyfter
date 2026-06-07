## Ejercicio 1 
# Cree un programa que lea un archivo con texto línea por línea, quite los saltos de línea (\n) y escriba todo el contenido en un solo renglón en un nuevo archivo
def read_lines(input_file):
    with open(input_file, 'r', encoding="utf-8") as f:
        return [line.strip() for line in f.readlines()]

def join_content(lines):
    return " ".join(lines)

def write_output(output_file, content):
    with open(output_file, 'w', encoding="utf-8") as f:
        f.write(content)

def run_exercise_1():
    input_file = input("Ingrese el archivo entrante: ")
    output_file = input("Ingrese el archivo saliente: ")

    try:
        lines = read_lines(input_file)
        content = join_content(lines)
        write_out(output_file, content)
        print(f"El archivo fue creado con existo y guardado en: {output_file}. ")
    except FileNotFoundError:
        print(f"Error: El archivo {input_file}, no existe. ")
    except Exception as e:
        print("Ocurrio un error: ", e)

def main():
    while True:
        print("\n--- Menu ---")
        print("1. Ejercicio 1 (Unir las lineas en una sola) ")
        print("2. Salir")
        
        choice = input("Seleccione una opción: ")
        
        if choice == "1":
            run_exercise_1()
        elif choice == "2":
            print("Proceso finalizado... ")
            break
        else:
            print("Opcion invalida. Intentelo de nuevo. ")

if __name__ == "__main__":
    main()


## Ejercicio 2 
# Cree un programa que abra un archivo de texto y cuente cuántas palabras contiene en total.
def count_words(filename):
    with open(filename, 'r', encoding="utf-8") as f:
        content = f.read()
    words = content.split()
    return len(words)

def run_exercise_2():
    filename = input("Ingrese el nombre del archivo: ")
    try:
        total = count_words(filename)
        print(f"El archivo contiene {total} palabras. ")
    except FileNotFoundError:
        print(f"Error: El archivo {filename}, no existe. ")
    except Exception as e:
        print(f"Ocurrio un error: ", e)

def main():
    while True:
        print("\n--- Menu ---")
        print("1. Ejercicio 2 (Contar las palabras de un archivo) ")
        print("2. Salir")
        
        choice = input("Seleccione una opcion: ")
        
        if choice == "1":
            run_exercise_2()
        elif choice == "2":
            print("Proceso finalizado...")
            break
        else:
            print("Opcion invalida. Intentelo de nuevo. ")

if __name__ == "__main__":
    main()


## Ejercicio 3 
# Cree un programa que: 1.Lea un archivo línea por línea / 2.Convierta cada línea a mayúsculas / 3.Escriba el contenido en un nuevo archivo.
def convert_to_uppercase(input_file, output_file):
    with open(input_file, 'r', encoding="utf-8") as f_in:
        lines = f_in.readlines()
    upper_lines = [line.strip().upper() for line in lines]
    
    with open(output_file, 'w', encoding="utf-8") as f_out:
        for line in upper_lines:
            f_out.write(line + "\n")
    
    return upper_lines

def run_exercise_3()
    input_file = input("Ingrese el nombre del archivo entrante: ")
    output_file = input("Ingrese el nombre del archivo saliente: ")
    try:
        result = convert_to_uppercase(input_file, output_file)
        print(f"El archivo fue convertido con existo y guardado en: {output_file}. ")
        print("Vista previa de las lineas convertidas: ")
        for line in result[:5]:
            print(line)
    except FileNotFoundError:
        print(f"Error: El archivo {input_file}, no existe. ")
    except Exception as e:
        print("Ocurrio un error: ", e)

def main():
    while True:
        print("\n--- Menu ---")
        print("1. Ejercicio 3 (convertir lineas a mayusculas) ")
        print("2. Salir")
        
        choice = input("Seleccione una opción: ")
        
        if choice == "1":
            run_exercise_3()
        elif choice == "2":
            print("Proceso finalizado... ")
            break
        else: 
            print("Opcion invalida. Intentelo de nuevo. ")

if __name__ == "__main__":
    main()


## Ejercicio 4
# Cree un programa que: 1.Pida al usuario una línea de texto / 2.Agregue esa línea al final de un archivo existente / 3.Si el archivo no existe, lo crea automáticamente.
def append_line(filename, text):
    try:
        with open(filename, 'a', encoding="utf-8") as f:
            f.write(text + "\n")
        return True
    except Exception as e: 
        raise RuntimeError(f"Error al agregar la linea: {e} ")

def run_exercise_4():
    filename = input("Ingrese el nombre del archivo: ")
    text = input("Ingrese una frase u oración: ")
    try:
        append_line(filename, text)
        print("La informacion fue añadida con exito al archivo. ")
    except RuntimeError as e:
        print(e)

def main():
    while True:
        print("\n--- Menu ---")
        print("1. Ejercicio 4 (Agregar linea al archivo) ")
        print("2. Salir")
        
        choice = input("Seleccione una opción: ")
        
        if choice == "1":
            run_exercise_4()
        elif choice == "2":
            print("Proceso finalizado...")
            break
        else:
            print("Opcion invalida. Intentelo de nuevo. ")

if __name__ == "__main__"
main()

