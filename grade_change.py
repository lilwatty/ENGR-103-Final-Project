
def display_grade():

    pass


def grade_change(student_schedule, grades, subject):

    # First check to see if the student is in the teacher's class
    student_schedule = list(student_schedule)

    if student_schedule.count(subject) == 0:
        print(f"This student is not enrolled in your course: {subject}")
        return
    else:
        period = student_schedule.index(subject)

        print(f'\n{subject}: {grades[period]}')

        decision = input("Enter Command:\n 1 - Change Grade\n 2 - Cancel\n")
        if decision == "1":
            new_grade = input("Enter New Grade: ")
            updated_grades = edit(new_grade, period, grades)
            return updated_grades

        return grades


def edit(new_grade, period, list_grades):
    new_list = list(list_grades).copy()
    new_list.pop(period)
    new_list.insert(period, new_grade)
    print("Grade successfully changed.")
    return new_list


'''
schedule = [
    "English Literature",
    "Biology",
    "Chemistry",
    "Computer Science",
    "Calculus",
    "Physics"
]
grades = [
    "A",
    "A",
    "B+",
    "A",
    "A-",
    "B+"
]
subject = 'Physics'

grade_change(schedule, grades, subject)
'''
