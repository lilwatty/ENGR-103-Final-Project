user_data = {
    "username": "123",
    "password": "123",
    "first_name": "sample",
    "last_name": "sample",
    "subject": "english",
    "permissions": "teacher"
}


def login():

    login_attempts = 0
    max_attempts = 3

    while login_attempts < max_attempts:

        user_attempt = input("Username: ")
        password_attempt = input("Password: ")

        for i in user_data:
            if user_attempt == user_data["username"]:
                if password_attempt == user_data["password"]:
                    return (i)

        else:
            login_attempts += 1
            print(
                f'Incorrect Credentials, {max_attempts - login_attempts} attempts left')
    print("Please try again later.")


login()
