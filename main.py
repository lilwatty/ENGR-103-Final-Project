import json
from local_data.data import convert_json_to_list
from display_commands import display_commands

from test_schedule import change_student_schedule
from final_report_card import display_report_card

from student_search import search_student
from enroll_student import enroll_student
from grade_change import grade_change

from login import login
from save_changes import save_dict_list_to_json

from schedule_change import change_student_schedule # since this is the main function, all other aspects are imported in


staff_registry = convert_json_to_list("local_data/employee_lists.txt")
student_registry = convert_json_to_list("local_data/student_files.txt") # converts the json lnformation to txt files for easier storage and reading

quick_login = [
    {
        "username": "123",
        "password": "123",
        "first_name": "Daniel",
        "last_name": "Perez",
        "subject": "Physics",
        "permissions": "teacher"
    },
] # default log in and password used for testing


for i in quick_login:
    staff_registry.append(i)


def main():

    user_data, login_status = login(staff_registry)
    user_data = dict(user_data)

    student = search_student(user_data, student_registry)
    student = dict(student) # main is the student and stagg registry here

    while login_status == True:
        display_commands(user_data['permissions']) #gives permissions if logged in

        command = (input("Enter Command: ")).lower() # enter commands C, R or L, maybe E depending on permissions

        if command == 'c' and user_data["permissions"] == "teacher":
            grade_list = grade_change(
                student['schedule'], student["grades"], user_data['subject'])
            student['grades'] = grade_list
            print(student['grades']) # C is listed as grade change command

        elif command == 'c' and user_data["permissions"] == "admin":
            new_schedule, new_grades = change_student_schedule(
                student)

        elif command == 'e' and user_data["permissions"] == "admin":
            new_student = enroll_student()
            student_registry.append(new_student) # ei in this case is enrolling a new student

        elif command == 'r':
            display_report_card(student) # displays report card of selected student

        elif command == 'l':
         with open("local_data/student_files.txt", "w") as file:
            json.dump(student_registry, file)
            file.flush()
            login_status = False # logs user out and saves data to txt file in local
            

        else:
            print("Invalid Input")


main()
