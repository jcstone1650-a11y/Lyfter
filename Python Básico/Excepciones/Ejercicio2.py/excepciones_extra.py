## Ejercicio 1
# Cree un programa que: pida el nombre y la edad.
def get_name():
    name = input("Ingrese su nombre: ")
    if name.isdigit():
        raise ValueError("El nombre no puede ser un numero. ")
    return name

def get_age():
    try:
        age = int(input("Ingrese su edad: "))
        return age 
    except ValueError:
        print("Dato invalido. ")
        return None

def show_result(name, age):
    print("----------------------------------")
    print(f"Hola {name}, su edad es {age}. ")
    print("----------------------------------")

def main():
    try: 
        name = get_name()
        age = get_age()
        if age is None:
            return 
        show_result(name, age)
    except ValueError as e:
        print(e)

main()


## Ejercicio 2 
# Cree una función convertir_a_entero(lista).
def convert_to_int(elements):
    for element in elements:
        try:
            converted = int(element)
            print(f'"{element}" convertido a {converted}. ')
        except ValueError:
            print(f"No se puede convertir el elemento: {element}. ")

def run_exercise_2():
    question = input("Ingrese la lista de elementos separados por un espacio. ")
    my_list = question.split()
    print("Resultado: ")
    convert_to_int(my_list) 

## Ejercicio 3 
# Cree una función sumar_valores(lista).
def sum_values(elements):
    total = 0.0
    for element in elements:
        try:
            value = float(element)
            total += value
            print(f"{value} sumado correctamente. ")
        except ValueError:
            print(f"Elemento invalido: '{element}'. ")
    print("---------------------------")
    print(f"La suma total es: {total}")
    print("---------------------------")

def run_exercise_3():
    user_input = input("Ingrese la lista de elementos separados por un espacio: ")
    my_list = user_input.split()
    print("Resultado: ")
    sum_values(my_list)

