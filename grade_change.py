#######################################################################
# Function: Grade Change
# Description: Teacher specific fuction that allows teacher to edit their student's grades.
# Parameters: student_schedule, grades, subject
# Return values: Returns a list of updated grades.
# Pre-Conditions: The user has successfully signed in and has the cridentials of a teacher.
# Post-Conditions: The student dictionary is updated with the new grade list.
#######################################################################


def grade_change(student_schedule, grades, subject):

    student_schedule = list(student_schedule)
    # Verify that teacher has student in their class
    if student_schedule.count(subject) == 0:

        print(f"This student is not enrolled in your course: {subject}")
        return

    else:
        # Index used in the idit function
        period = student_schedule.index(subject)

        print(f'\n{subject}: {grades[period]}')

        decision = input("Enter Command:\n 1 - Change Grade\n 2 - Cancel\n")
        if decision == "1":
            new_grade = input("Enter New Grade: ")
            updated_grades = edit_list(new_grade, period, grades)
            return updated_grades

        return grades

#######################################################################
# Function: Edit List
# Description: Custom function that replaces a list value at a given index.
# Parameters: New_grade, Index, and previous list.
# Return values: New list.
# Pre-Conditions: The passed values are lists or strings.
# Post-Conditions: The updated grades will replace the previous grades.
#######################################################################


def edit_list(new_grade, period, list_grades):

    # Type conversion to access list methods
    new_list = list(list_grades).copy()
    new_list.pop(period)
    new_list.insert(period, new_grade)

    print("Grade successfully changed.")  # Success
    return new_list
