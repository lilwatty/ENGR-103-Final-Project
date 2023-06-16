from login import login
from student_search import search_student
# from enroll_student import enroll_student
from grade_change import grade_change
# from report_card_generator import display_report_card
from schedule_change import change_student_schedule

from display_commands import display_commands
from local_data.data import convert_json_to_list

staff_registry = convert_json_to_list("local_data/employee_lists.txt")
student_registry = convert_json_to_list("local_data/student_files.txt")

quick_login = [
    {
        "username": "123",
        "password": "123",
        "first_name": "Daniel",
        "last_name": "Perez",
        "subject": "Physics",
        "permissions": "admin"
    },
]


for i in quick_login:
    staff_registry.append(i)


def main():
    user_data, login_status = login(staff_registry)
    user_data = dict(user_data)

    student = search_student(user_data, student_registry)
    student = dict(student)

    while login_status == True:
        display_commands(user_data['permissions'])

        command = (input("Enter Command: ")).lower()

        if command == 'c' and user_data["permissions"] == "teacher":
            grade_list = grade_change(
                student['schedule'], student["grades"], user_data['subject'])
            student['grades'] = grade_list
            print(student['grades'])

        elif command == 'c' and user_data["permissions"] == "admin":
            new_schedule = change_student_schedule(
                student, list(student['schedule']))

        elif command == 'e' and user_data["permissions"] == "admin":
            pass

        elif command == 'l':
            quit()
        else:
            print("Invalid Input")


main()
