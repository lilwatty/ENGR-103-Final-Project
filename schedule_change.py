from data_generation.raw_data import classes

student = {
    "first_name": "Adam",
    "last_name": "Watson",
    "ID": "934472703",
    "sex": "Male",
    "DOB": "04/20/1969",
    "schedule": [
        "English Literature",
        "Biology",
        "Chemistry",
        "Computer Science",
        "Calculus",
        "Physics"
    ],
    "grades": [
        "A",
        "A",
        "B+",
        "A",
        "A-",
        "B+"
    ],
    "active": True
}

def change_student_schedule(student, classes):

    print(student['schedule'])  # display the students schedule in array form

    # user inputs what class they want to change
    old_class = int(input(
        "Type in the index number of the class you want to change (keep in mind the first class is 0): "))

    # user confirms that they want to change the class
    confirmation = str(input(
        "Are you sure you want to change this class? The student's grade data will be lost. yes or no: "))

    if (confirmation.lower() == "no"):  # If the user inputs no, exits the function

        print("Schedule change aborted.")

    elif (confirmation.lower() == "yes"):  # If user inputs yes, continue changing the schedule

        clear_grade = "-"  # creates value to change the grade to to clear it
        print(classes)  # Display the possible classes to the user
        # User inputs the class they want to change to
        new_class = int(input(
            "Type in the index number of the class you want to change it to (keep in mind the first class is 0): "))

        # change the old class to the new one
        student['schedule'][old_class] = classes[new_class]
        # wipe student's grade data for that class slot
        student['grades'][old_class] = clear_grade

        print(student['schedule'])
        print(student['grades'])

    else:  # If the user enters an invalid input, inform them and exit the

        print("Invalid input")


change_student_schedule(student,classes)
