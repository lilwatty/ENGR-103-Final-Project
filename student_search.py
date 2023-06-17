
from local_data import data
students = data.student_registry


def search_student(user_data, list):

    searched_student = input("Enter student first and last name: ") # takes first and last name as input

    first_name, last_name = split_name(searched_student)
    student_info = fetch_data(first_name, last_name, list) #finds student with given info

    if student_info == None:
        search_student()

    elif student_info['active'] == False and user_data["permissions"] == "teacher":

        print("Student not found in current registry.") # bad case given if no student is found

    else:

        print(student_info) # good case where student is found and information is printed

        return student_info


def split_name(name):

    try:
        full_name = name.lower().rsplit(" ") # program will work even if there is no space between first and last name

        first = full_name[0]
        last = full_name[1]

    except:

        return split_name(input("Enter First and Last name: "))

    return first, last


def fetch_data(attempt_first_name, attempt_last_name, list):

    results = []
    for i in list:

        student_first_name = i["first_name"]
        student_last_name = i["last_name"]

        if student_first_name.lower() == attempt_first_name.lower():
            if student_last_name.lower() == attempt_last_name.lower():
                results.append(i)
                return results[0] # will return if no results are matching

        else:
            continue

    print("Student not found.") # uh oh bad case no student, will return
    return None
