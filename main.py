import csv

FILE = "students.csv"


def add_student():
    roll = input("Enter roll number: ")
    name = input("Enter student name: ")
    python = float(input("Enter Python marks: "))
    maths = float(input("Enter Maths marks: "))
    english = float(input("Enter English marks: "))

    total = python + maths + english
    average = total / 3

    if average >= 90:
        grade = "A+"
    elif average >= 80:
        grade = "A"
    elif average >= 70:
        grade = "B"
    elif average >= 60:
        grade = "C"
    elif average >= 50:
        grade = "D"
    else:
        grade = "F"

    with open(FILE, "a", newline="") as file:
        writer = csv.writer(file)

        if file.tell() == 0:
            writer.writerow(
                ["Roll No", "Name", "Python", "Maths", "English",
                 "Total", "Average", "Grade"]
            )

        writer.writerow(
            [roll, name, python, maths, english,
             total, round(average, 2), grade]
        )

    print("Student added successfully.")


def show_students():
    try:
        with open(FILE, "r") as file:
            reader = csv.reader(file)

            for row in reader:
                print(row)

    except FileNotFoundError:
        print("No student records found.")


def search_student():
    roll = input("Enter roll number to search: ")

    try:
        with open(FILE, "r") as file:
            reader = csv.DictReader(file)

            found = False

            for student in reader:
                if student["Roll No"] == roll:
                    print("\nStudent Details")
                    print("Name:", student["Name"])
                    print("Python:", student["Python"])
                    print("Maths:", student["Maths"])
                    print("English:", student["English"])
                    print("Total:", student["Total"])
                    print("Average:", student["Average"])
                    print("Grade:", student["Grade"])
                    found = True

            if not found:
                print("Student not found.")

    except FileNotFoundError:
        print("No student records found.")


def analyze_performance():
    try:
        with open(FILE, "r") as file:
            reader = csv.DictReader(file)

            students = list(reader)

            if len(students) == 0:
                print("No student records found.")
                return

            total_marks = 0
            highest = students[0]

            for student in students:
                total_marks += float(student["Average"])

                if float(student["Average"]) > float(highest["Average"]):
                    highest = student

            class_average = total_marks / len(students)

            print("\nPerformance Analysis")
            print("Number of students:", len(students))
            print("Class average:", round(class_average, 2))
            print("Top student:", highest["Name"])
            print("Top student average:", highest["Average"])

    except FileNotFoundError:
        print("No student records found.")


def main():
    while True:
        print("\nStudent Performance Management System")
        print("1. Add Student")
        print("2. Show All Students")
        print("3. Search Student")
        print("4. Analyze Performance")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_student()

        elif choice == "2":
            show_students()

        elif choice == "3":
            search_student()

        elif choice == "4":
            analyze_performance()

        elif choice == "5":
            print("Thank you.")
            break

        else:
            print("Invalid choice.")


main()
