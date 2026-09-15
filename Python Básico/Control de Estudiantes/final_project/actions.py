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
    