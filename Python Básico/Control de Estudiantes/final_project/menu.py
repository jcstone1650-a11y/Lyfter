from actions import (
    add_student, 
    list_students, 
    top_students, 
    average_all,
    show_failed_students, 
    delete_student
)
from data import export_data, import_data

def show_menu(students):
    while True:
        print("\n--- Sistema de Control de Estudiantes ---")
        print()
        print("1. Agregar estudiante")
        print("2. Lista de estudiantes")
        print("3. Mostrar los primeros 3 promedios")
        print("4. Mostrar promedio individual de cada estudiante")
        print("5. Exportar la informacion en CSV")
        print("6. Importar la inforamcion en CSV")
        print("7. Estudiantes reprobados")
        print("8. Eliminar estudiante")
        print("9. Salir")

        print()
        choice = input("Seleccione una opción: ")

        if choice == "1":
            add_student(students)
        elif choice == "2":
            list_students(students)
        elif choice == "3":
            top_students(students)
        elif choice == "4":
            average_all(students)
        elif choice == "5":
            export_data(students)
        elif choice == "6":
            import_data(students)
        elif choice == "7":
            show_failed_students(students)
        elif choice == "8":
            delete_student(students)
        elif choice == "9":
            print("Adios!")
            break
        else:
            print("\n")
            print("-" * 36)
            print("Error. Por favor inténtelo de nuevo.")
            print("-" * 36)