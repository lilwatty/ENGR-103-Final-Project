
import random
from local_data.data import student_registry

#######################################################################
"""
Function: unique_id_checker
Description: Checks that created ID is not already assigned to a student in the student registr
Parameters: "created" is a parameter that is filled with the created ID and used in the function to check against existing student IDs
Return values: created
Pre-Conditions: Parameter must be filled with ID, unique_id_checker is called
Post-Conditions: A unique student ID must be returned
"""
#######################################################################


def unique_id_checker(created):
    for i in student_registry:
        id = i["ID"]  # finds listed student ID in dictionary
        if created == id:  # creates new ID if previous is already in use
            generate_id()
        else:
            return created


#######################################################################
"""
Function: generate_id
Description: Generates a unique nine-character string starting with 934 that serves as a student ID
Parameters: None
Return values: unique_id
Pre-Conditions: generate_id is called
Post-Conditions: Unique student ID is returned
"""
#######################################################################


def generate_id():
    num_set1 = str(random.randint(100, 999))
    num_set2 = str(random.randint(100, 999))
    # combines randomly generated strings with 934 prefix
    id = "934-" + num_set1 + "-" + num_set2

    unique_id = unique_id_checker(id)
    return unique_id
