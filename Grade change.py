from data.data_generator import student_registry

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