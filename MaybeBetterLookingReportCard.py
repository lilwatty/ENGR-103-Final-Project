from tkinter import Tk, Label, Frame


def display_report_card(student):

    # Create a Tkinter window
    window = Tk()
    window.title("Report Card")

    # Create a frame to hold the report card information
    frame = Frame(window)
    frame.pack()

    # Create labels to display the student's information
    Label(frame, text="Name:").grid(row=0, column=0)
    Label(frame, text=(student['first_name'] +
          student['last_name'])).grid(row=0, column=1)

    Label(frame, text="ID:").grid(row=1, column=0)
    Label(frame, text=student['ID']).grid(row=1, column=1)

    # Display the grades in separate rows
    Label(frame, text="Grades:").grid(row=2, column=0)
    grades = student['grades']
    for i, grade in enumerate(grades):
        Label(frame, text=grade).grid(row=2 + i, column=1)

    # Display the window
    window.mainloop()