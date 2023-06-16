def login(user_data):

    login_attempts = 0
    max_attempts = 3

    while login_attempts < max_attempts:

        user_attempt = input("Username: ")
        password_attempt = input("Password: ")

        for i in user_data:
            if user_attempt == i["username"]:
                if password_attempt == i["password"]:
                    logged_in = True
                    return i, logged_in

        else:
            login_attempts += 1
            print(
                f'Incorrect Credentials, {max_attempts - login_attempts} attempts left')
    print("Please try again later.")
