#######################################################################
# Function: Login
# Description: Accesses teacher database and checks to see if user enter in the proper login cridentials.
# Parameters: Staff registry
# Return values: Specific dictionary and changes logged in to be True.
# Pre-Conditions: The staff registry is in the form a list of dictionaries.
# Post-Conditions: None
#######################################################################


def login(staff_registry):

    login_attempts = 0
    max_attempts = 3

    while login_attempts < max_attempts:

        user_attempt = input("Username: ")
        password_attempt = input("Password: ")

        # Checks to see if the username matches on in the registry.
        for i in staff_registry:
            if user_attempt == i["username"]:
                # Does password match username?
                if password_attempt == i["password"]:
                    logged_in = True
                    return i, logged_in

        else:
            login_attempts += 1  # Maintains security
            print(
                f'Incorrect Credentials, {max_attempts - login_attempts} attempts left')
    print("Please try again later.")
