import csv

FILENAME = "students.csv"

def export_data(students):
    if not students:
        print("No hay datos para exportar.")
        print()
        return
    with open(FILENAME, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Name", "Section", "Español", "Ingles", "Estudios Sociales", "Ciencias"])
        for s in students:
            writer.writerow([s["name"], s["section"], *s["grades"].values()])
    print("\nInformación exportada con éxito.")
    print()

def import_data(students):
    try:
        students.clear()
        with open(FILENAME, "r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                grades = {
                    "Español": int(row["Español"]),
                    "Ingles": int(row["Ingles"]),
                    "Estudios Sociales": int(row["Estudios Sociales"]),
                    "Ciencias": int(row["Ciencias"])
                }
                students.append({"name": row["Name"], "section": row["Section"], "grades": grades})
        print("\nInformación importada con éxito.")
        print()
    except FileNotFoundError:
        print("Archivo no encontrado. Por favor exporte los datos primero.")
        print()