import csv
from actions import students

FILENAME = "students.csv"

def export_data():
    if not students:
        print("No data to export.")
        return
    with open(FILENAME, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Name", "Section", "Spanish", "English", "Social Studies", "Science"])
        for s in students:
            writer.writerow([s["name"], s["section"], *s["grades"].values()])
    print("Data exported successfully.")

def import_data():
    try:
        with open(FILENAME, "r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                grades = {
                    "Spanish": int(row["Spanish"]),
                    "English": int(row["English"]),
                    "Social Studies": int(row["Social Studies"]),
                    "Science": int(row["Science"])
                }
                students.append({"name": row["Name"], "section": row["Section"], "grades": grades})
        print("Data imported successfully.")
    except FileNotFoundError:
        print("No CSV file found. Please export data first.")

