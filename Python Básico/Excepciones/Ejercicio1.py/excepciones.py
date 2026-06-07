## Ejercicio 1 
# Cree una calculadora por linea de comando. Esta debe de tener un número actual, y un menú para decidir qué operación hacer con otro número:

#Creamos las funciones
def add(current, number):
    return current + number

def subtract(current, number):
    return current - number

def multiply(current, number):
    return current * number 

def divide(current, number):
    if number == 0:
        print("Error. No se puede dividir entre cero. ")
        return current
    return current / number 

def reset():
    return 0.0

#Creamos el menu
def show_menu(current):
    print("\nNumero actual es: ", current)
    print("\n--- Menu ---")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")
    print("5. Borrar resultado (reset)")
    print("6. Salir")

#Codigo principal
def calculator():
    current = 0.0
    while True:
        show_menu(current)
        choice = input("Elija una opción: ")
        
        if choice == "6":
            print("\nFinalizando proceso. ")
            print("______________________")
            break
        
        elif choice == "5":
            current = reset()
            print("\nResultado borrado. El nuevo numero es 0. ")
            print("---------------------------------------")
            continue
        
        elif choice in ["1", "2", "3", "4"]:
            try:
                new_number = float(input("Ingrese el nuevo numero: "))
            except ValueError:
                print("Error: Ingrese un numero valido. ")
                continue 
            
            if choice == "1":
                current = add(current, new_number)
            elif choice == "2":
                current = subtract(current, new_number)
            elif choice == "3":
                current = multiply(current, new_number)
            elif choice == "4":
                current = divide(current, new_number)
                
        else:
            print("\nError. Elija una opción valida. ")
            print("--------------------------------")
            
calculator()





