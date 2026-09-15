main.py
---------
from menu import show_menu

def main():
    show_menu()

if __name__ == "__main__":
    main()


menu.py
--------
from actions import (
    add_student, list_students, top_students, average_all,
    show_failed_students, delete_student
)
from data import export_data, import_data

def show_menu():
    while True:
        print("\n--- Student Management System ---")
        print("1. Add student")
        print("2. List students")
        print("3. Show top 3 students")
        print("4. Show average grade of all students")
        print("5. Export data to CSV")
        print("6. Import data from CSV")
        print("7. Show failed students")
        print("8. Delete student")
        print("9. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            add_student()
        elif choice == "2":
            list_students()
        elif choice == "3":
            top_students()
        elif choice == "4":
            average_all()
        elif choice == "5":
            export_data()
        elif choice == "6":
            import_data()
        elif choice == "7":
            show_failed_students()
        elif choice == "8":
            delete_student()
        elif choice == "9":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")


actions.py
---------
import re

students = []

def is_valid_name(name):
    return bool(name.strip()) and not any(char.isdigit() for char in name)

def is_valid_section(section):
    return re.match(r"^\d{2}[A-Z]$", section) is not None

def is_valid_grade(grade):
    return 0 <= grade <= 100

def student_exists(name, section):
    return any(s for s in students if s["name"] == name and s["section"] == section)

def add_student():
    name = input("Enter full name: ")
    if not is_valid_name(name):
        print("Invalid name.")
        return

    section = input("Enter section (e.g., 11B): ")
    if not is_valid_section(section):
        print("Invalid section format.")
        return

    if student_exists(name, section):
        print("Student already exists.")
        return

    grades = {}
    for subject in ["Spanish", "English", "Social Studies", "Science"]:
        while True:
            try:
                grade = int(input(f"Enter {subject} grade (0-100): "))
                if is_valid_grade(grade):
                    grades[subject] = grade
                    break
                else:
                    print("Grade must be between 0 and 100.")
            except ValueError:
                print("Invalid input. Enter a number.")

    students.append({"name": name, "section": section, "grades": grades})
    print("Student added successfully.")

def list_students():
    if not students:
        print("No students registered.")
        return
    for s in students:
        print(f"{s['name']} ({s['section']}) - {s['grades']}")

def calculate_average(student):
    return sum(student["grades"].values()) / len(student["grades"])

def top_students():
    if not students:
        print("No students registered.")
        return
    sorted_students = sorted(students, key=calculate_average, reverse=True)
    for s in sorted_students[:3]:
        print(f"{s['name']} ({s['section']}) - Avg: {calculate_average(s):.2f}")

def average_all():
    if not students:
        print("No students registered.")
        return
    avg = sum(calculate_average(s) for s in students) / len(students)
    print(f"Overall average: {avg:.2f}")

def show_failed_students():
    failed = []
    for s in students:
        failed_subjects = {sub: grade for sub, grade in s["grades"].items() if grade < 60}
        if failed_subjects:
            failed.append((s["name"], s["section"], failed_subjects))
    if not failed:
        print("No failed students.")
    else:
        for name, section, subjects in failed:
            print(f"{name} ({section}) failed: {subjects}")

def delete_student():
    name = input("Enter student name to delete: ")
    section = input("Enter section: ")
    for s in students:
        if s["name"] == name and s["section"] == section:
            confirm = input("Are you sure? (y/n): ")
            if confirm.lower() == "y":
                students.remove(s)
                print("Student deleted.")
            return
    print("Student not found.")



data.py
-------
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




#USO DE PYTEST 

!pip install pytest 

import pytest
from actions import (
    is_valid_name, is_valid_section, is_valid_grade,
    calculate_average, student_exists, students
)

def test_is_valid_name():
    assert is_valid_name("John Doe")
    assert not is_valid_name("")  # empty name
    assert not is_valid_name("John123")  # contains numbers

def test_is_valid_section():
    assert is_valid_section("11B")
    assert is_valid_section("10A")
    assert not is_valid_section("A11")  # wrong format
    assert not is_valid_section("11")   # missing letter

def test_is_valid_grade():
    assert is_valid_grade(0)
    assert is_valid_grade(100)
    assert not is_valid_grade(-1)
    assert not is_valid_grade(101)

def test_calculate_average():
    student = {
        "name": "Jane Doe",
        "section": "11B",
        "grades": {"Spanish": 80, "English": 90, "Social Studies": 70, "Science": 100}
    }
    avg = calculate_average(student)
    assert avg == pytest.approx(85.0)

def test_student_exists():
    students.clear()
    students.append({"name": "Jane Doe", "section": "11B", "grades": {}})
    assert student_exists("Jane Doe", "11B")
    assert not student_exists("John Doe", "11B")

