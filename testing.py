user_data = [
    {
        "username": "tekadrad",
        "password": "radhika123",
        "first_name": "Radhika",
        "last_name": "Tekade",
        "subject": "Computer Science",
        "permissions": "teacher"
    },
    {
        "username": "sharmdee",
        "password": "deepak123",
        "first_name": "Deepak",
        "last_name": "Sharma",
        "permissions": "admin"
    }
]


def login(user_data):

    login_attempts = 0
    max_attempts = 3

    while login_attempts < max_attempts:

        user_attempt = input("Username: ")
        password_attempt = input("Password: ")
        for i in user_data:
            if user_attempt == i["username"]:
                if password_attempt == i["password"]:
                    print(i)
        else:
            login_attempts += 1
            print(
                f'Incorrect Credentials, {max_attempts - login_attempts} attempts left')
    print("Please try again later.")


login(user_data)
