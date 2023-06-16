def display_commands(permissions):
    if permissions == "teacher":
        print("Enter Command:\n C - Change Grade")
    else:
        print("Enter Command:\n C - Change Schedule\n E - Enroll Student")

    print(" R - Display Report Card\n L - Log Out\n")


display_commands("teacher")
