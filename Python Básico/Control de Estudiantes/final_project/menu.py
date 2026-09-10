from actions import (
    add_student, 
    list_students, 
    top_students, 
    average_all,
    show_failed_students, 
    delete_student
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