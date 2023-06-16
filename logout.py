def logout(command):
    while True:
        print((input("type exit to logout")))
        if command == 'exit':
            from login import login