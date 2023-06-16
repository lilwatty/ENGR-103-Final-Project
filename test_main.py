from login import login
from student_search import search_student
# from enroll_student import enroll_student
from test_grade_change import grade_change
# from report_card_generator import display_report_card
# from schedule_change import schedule_change

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
        "permissions": "teacher"
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

        if user_data["permissions"] == "teacher":

            if command == 'c':

                grade_list = grade_change(student['schedule'],
                                          student["grades"], user_data['subject'])
                print(grade_list)

        elif command == 'l':
            break

        else:
            print("Invalid Input")


main()
