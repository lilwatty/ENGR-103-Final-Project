from local_data.data import staff_registry, student_registry
from generate_id import generate_id

#######################################################################
# Function: enroll_student
# Description: prompts user for student information, assigns information to variables, compiles variables into dictionary formatted to match student registry
# Parameters: None
# Return values: student_profile
# Pre-Conditions: enroll_student must be called
# Post-Conditions: student profile with user inputs is returned
#######################################################################

def enroll_student():
    while True: # assigns user inputs to variables and then asks user to verify
        first_name = input(
            "Enter New Student Information Below\nFirst Name: ")
        last_name = input("Last Name: ") # asks for first and last name
        sex = input("Gender: ")
        dob = input("Date-Of-Birth: ") # more information on new student
        schedule, grades = create_schedule()
        user_decision = input(
            "Please Verify New Student Information\nFinalize New Student Profile? (y/n): ") #asking for confirmation
        if user_decision == "n": # passes through 
            pass
        elif user_decision == "y": # completes enrollment
            break
    student_profile = { # dictionary formatted to match student profiles in student registry
        "first_name": first_name,
        "last_name": last_name,
        "ID": generate_id(),
        "sex": sex,
        "DOB": dob,
        "schedule": schedule,
        "grades": grades,
        "active": True, # adds all information and sets student active
    }
    return student_profile

#######################################################################
# Function: create_schedule
# Description: Continually prompts user to input student classes, stops when specified key is entered, creates blank grades to match schedule
# Parameters: None
# Return values: schedule and grades
# Pre-Conditions: create_schedule must be called
# Post-Conditions: schedule of user inputs is returned, equivalent amount of blank grades are returned
#######################################################################

def create_schedule():
    schedule = [] # creating empty lists for schedule and grades
    grades = []
    while True:
        if len(schedule) == 6: # sets maximum amount of classes
            break
        student_class = input(
            "Enter Classes (Input 'X' When Finalized): ")
        if student_class == "X": # stops asking user for inputs
            break
        schedule.append(student_class) # adds inputs to list
    for i in range(len(schedule)): # creates a matching amount of blank grades
        grades.append("_")
    return schedule, grades
