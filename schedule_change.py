from data_generation.raw_data import classes


def change_student_schedule(student):

    print(student['schedule'])  # display the students schedule in array form

    # user inputs what class they want to change
    old_class = int(input(
        "Type in the index number of the class you want to change (keep in mind the first class is 0): "))

    # user confirms that they want to change the class
    confirmation = (input(
        "Are you sure you want to change this class? The student's grade data will be lost. yes or no: "))

    if (confirmation.lower() == "no"):  # If the user inputs no, exits the function

        print("Schedule change aborted.")

    elif (confirmation.lower() == "yes"):  # If user inputs yes, continue changing the schedule

        clear_grade = "-"  # creates value to change the grade to to clear it
        print(classes)  # Display the possible classes to the user
        # User inputs the class they want to change to
        new_class = int(input(
            "Type in the index number of the class you want to change it to (keep in mind the first class is 0): "))

        schedule = list(student['schedule'])
        schedule.pop(int(old_class))
        schedule.insert(new_class, classes[new_class])
        print(f'New Schedule: {schedule}')
        return schedule

    else:  # If the user enters an invalid input, inform them and exit the

        print("Invalid input")
