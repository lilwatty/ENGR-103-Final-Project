from data.student_data import student_registry
from login import user_data


def student_search():

    searched_student = input("Enter student first and last name: ")

    first_name, last_name = split_name(searched_student)
    student_info = fetch_data(first_name, last_name, student_registry)

    if student_info == None:
        student_search()

    elif student_info['active'] == False and user_data["permissions"] == "teacher":

        print("Student not found in current registry.")

    else:

        print(student_info)

        return student_info


def split_name(name):

    try:
        full_name = name.lower().rsplit(" ")

        first = full_name[0]
        last = full_name[1]

    except:
        print("Enter First and Last name.")
        student_search()

    return first, last


def fetch_data(attempt_first_name, attempt_last_name, list):

    results = []
    for i in list:

        student_first_name = i["first_name"]
        student_last_name = i["last_name"]

        if student_first_name.lower() == attempt_first_name.lower() and student_last_name.lower() == attempt_last_name.lower():
            results.append(i)
            return results[0]

        else:
            continue

    print("Student not found.")
    return None


def main():
    student_search()


main()