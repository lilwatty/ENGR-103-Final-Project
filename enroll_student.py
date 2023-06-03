from local_data.data import staff_registry, student_registry
from generate_id import generate_id


def enroll_student():
    while True:
        first_name = input("Enter New Student Information Below\nFirst Name: ")
        last_name = input("Last Name: ")
        sex = input("Gender: ")
        dob = input("Date-Of-Birth: ")
        while True:
            schedule = []
            grades = []
            while True:
                student_class = input(
                    "Enter Classes (Input 'X' When Finalized): ")
                if student_class == "X":
                    break
                schedule.append(student_class)
            while True:
                class_grade = input(
                    "Enter Grades (Input 'X' When Finalized): ")
                if class_grade == "X":
                    break
                grades.append(class_grade)
            if len(schedule) == len(grades):
                break
            else:
                print(
                    "Invalid Attempt\nReason: Class And Grade Quantites Are Not Equal\nPlease Try Again")
                pass
        user_decision = input(
            "Please Verify New Student Information\nFinalize New Student Profile? (y/n): ")
        if user_decision == "n":
            pass
        elif user_decision == "y":
            break
    student_profile = {
        "first_name": first_name,
        "last_name": last_name,
        "id": generate_id(),
        "sex": sex,
        "DOB": dob,
        "schedule": schedule,
        "grades": grades,
        "active": True
    }
    student_registry.append(student_profile)


enroll_student()
