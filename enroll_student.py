from local_data.data import staff_registry, student_registry
from generate_id import generate_id


def enroll_student():
    while True:
        first_name = input(
            "Enter New Student Information Below\nFirst Name: ")
        last_name = input("Last Name: ")
        sex = input("Gender: ")
        dob = input("Date-Of-Birth: ")
        schedule, grades = create_schedule()
        user_decision = input(
            "Please Verify New Student Information\nFinalize New Student Profile? (y/n): ")
        if user_decision == "n":
            pass
        elif user_decision == "y":
            break
    student_profile = {
        "first_name": first_name,
        "last_name": last_name,
        "ID": generate_id(),
        "sex": sex,
        "DOB": dob,
        "schedule": schedule,
        "grades": grades,
        "active": True,
    }
    student_registry.append(student_profile)


def create_schedule():
    schedule = []
    grades = []
    while True:
        if len(schedule) == 6:
            break
        student_class = input(
            "Enter Classes (Input 'X' When Finalized): ")
        if student_class == "X":
            break
        schedule.append(student_class)
    for i in range(len(schedule)):
        grades.append("_")
    return schedule, grades
