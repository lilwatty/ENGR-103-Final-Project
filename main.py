from login import login
from student_search import search_student
from enroll_student import enroll_student
from change_grade import change_student_grade
from report_card_generator import display_report_card
from schedule_change import schedule_change

from local_data.data import staff_registry, student_registry

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


for i in quick_login:
    staff_registry.append(i)


def main():
    user_data, login_status = login(staff_registry)

    while login_status == True:

        student = search_student(user_data, student_registry)

        command = (input("Enter Command: ")).lower()

        if user_data["permissions"] == "teacher":

            if command == 'c':

                change_student_grade(student)

        if user_data["permissions"] == "admin":

            if command == 'e':
                enroll_student(student)

            elif input == 's':
                schedule_change(student)

        elif command == 'p':
            display_report_card(student)

        elif command == 'l':
            break

        else:
            print("Invalid Input")


main()
