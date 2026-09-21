import re

SUBJECTS = [
    "Español",
    "Ingles",
    "Estudios Sociales",
    "Ciencias"
]

def is_valid_name(name):
    return bool(
        re.match(
            r"^[A-Za-zÁÉÍÓÚáéíóúÑñ ]+$",
            name.strip()
            )
        )

def is_valid_section(section):
    return re.match(
        r"^\d{2}[A-Z]$",
        section)is not None

def is_valid_grade(grade):
    return 0 <= grade <= 100

def student_exists(students, name, section):
    return any(
        s["name"] == name and s["section"] == section for s in students
        )

def get_grade(subject):
        while True:
            try:
                grade = int(input(f"Ingrese la calificación de {subject} (0-100): "))
                if is_valid_grade(grade):
                    return grade
                
                else:
                    print("La calificación debe estar entre 0 y 100.")
                    
            except ValueError:
                print("Error. Ingrese un número.")

def add_student(students):
    name = input("Ingrese el nombre completo: ")
    
    if not is_valid_name(name):
        print("Nombre inválido.")
        return

    section = input("Ingrese la sección (e.j., 11B): ")
    
    if not is_valid_section(section):
        print("Formato de sección no válido.")
        return

    if student_exists(students, name, section):
        print("El estudiante ya existe.")
        return

    grades = {}
    
    for subject in SUBJECTS:
        grades[subject] = get_grade(subject)
        
    students.append(
        {
            "name": name,
            "section": section,
            "grades": grades
        }
    )
    print("-" * 30)
    print("Estudiante agregado con éxito.")
    print("-" * 30)

def list_students(students):
    if not students:
        print("No hay estudiantes registrados.")
        return
    
    for s in students:
        print(f"\nNombre: {s['name']}")
        print(f"Sección: {s['section']}")
        
        for subject, grade in s["grades"].items():
            print(f" {subject}: {grade}")

        print("-" * 30)
        print()

def calculate_average(student):
    return sum(student["grades"].values()) / len(student["grades"])

def top_students(students):
    if not students:
        print("No hay estudiantes registrados.")
        return
    sorted_students = sorted(students, key=calculate_average, reverse=True)
    for s in sorted_students[:3]:
        print(f"\n{s['name']} ({s['section']}) - Promedio: {calculate_average(s):.2f}")
        print()

def average_all(students):
    if not students:
        print("No hay estudiantes registrados.")
        return
    
    for s in students:
        avg = calculate_average(s)
        print(f"\n{s['name']} ({s['section']}) - Promedio: {avg:.2f}")
        print()

def show_failed_students(students):
    failed = []
    for s in students:
        failed_subjects = {sub: grade for sub, grade in s["grades"].items() if grade < 60}
        if failed_subjects:
            failed.append((s["name"], s["section"], failed_subjects))
    if not failed:
        print("\nNo hay estudiantes reprobados.")
        print()
    else:
        for name, section, subjects in failed:
            print(f"{name} ({section}) fallido: {subjects}")
            print()

def delete_student(students):
    name = input("Ingrese el nombre del estudiante: ")
    section = input("Confirme la sección: ")
    
    found = False
    
    for s in students:
        if s["name"] == name and s["section"] == section:
            found = True
            
            confirm = input("Estas seguro? (si/no): ")
            
            if confirm.strip().lower() in ("si", "s"):
                students.remove(s)
                
                print("-" * 30)
                print("Estudiante eliminado con éxito.")
                print("-" * 30)
                print()
                
            elif confirm.strip().lower() in ("no", "n"): 
                print()
                print("Operación cancelada.")
                print()
            else:           
                print()
                print("Opción no válida.")
                print()
            break
        
    if not found:
        print()
        print("Error. El estudiante no existe, inténtelo de nuevo.")
        print()