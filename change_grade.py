from local_data.data import student_registry
from login import login

quick_login = [
    {
        "username": "123",
        "password": "123",
        "first_name": "Daniel",
        "last_name": "Perez",
        "subject": "Statistics",
        "permissions": "teacher"
    },
]

# Your code needs to take in the user_data["subject"] as a parameter and only allow the teacher to change
# the grade for their class. Accessing the student by ID is good. Keep in mind, the teacher would have
# looked them up already in the search student file


def change_student_grade(student_id, new_grade):
    # Check if the student ID exists in the registry
    if student_id not in student_registry:
        print("Student ID not found.")
        return

    # Update the student's grade
    student_registry[student_id]['grade'] = new_grade
    print("Grade updated successfully.")


# User inputs
student_id = input("Enter the student ID: ")
new_grade = input("Enter the new grade: ")

change_student_grade(student_id, new_grade)
