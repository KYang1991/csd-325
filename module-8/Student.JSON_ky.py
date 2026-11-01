"""CSD-325 Module 8 - JSON Practice
Student: Kao Yang
"""

import json
from pathlib import Path

# Keep Student.json in the same folder as this Python script.
file_path = Path(__file__).with_name("Student.json")


def print_students(students):
    """Display each student's name, ID, and email."""
    for student in students:
        print(
            f"{student['L_Name']}, {student['F_Name']} : "
            f"ID = {student['Student_ID']} , Email = {student['Email']}"
        )


def main():
    # Load the existing JSON array into a Python list.
    with file_path.open("r", encoding="utf-8") as student_file:
        students = json.load(student_file)

    print("Original Student List:")
    print_students(students)

    # Add a new student to the list.
    students.append({
        "F_Name": "Kao",
        "L_Name": "Yang",
        "Student_ID": 98765,  # Fictional ID
        "Email": "kao.yang@csd325.com",  # Fictional email
    })

    print("\nUpdated Student List:")
    print_students(students)

    # Save the complete updated list as valid JSON.
    with file_path.open("w", encoding="utf-8") as student_file:
        json.dump(students, student_file, indent=4)

    print("\nStudent.json file was updated.")


if __name__ == "__main__":
    main()
