from tkinter import Tk, Label, Frame
from local_data.data import student_registry
# from login import user_data

student = [
    {
        "first_name": "Eilman",
        "last_name": "Karim",
        "id": "123",
        "sex": "Male",
        "DOB": "01/27/2004",
        "schedule": [
            "Physical Education",
            "Botany",
            "Gender Studies",
            "Pilates",
            "Buisness",
            "Physics"
        ],
        "grades": [
            "C",
            "C-",
            "D",
            "A+",
            "C-",
            "L"
        ],
        "active": True
    }
]


def display_report_card(students):
    # Get the student details from the student registry
    for i in students:
        student = i

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
    Label(frame, text=student['id']).grid(row=1, column=1)

    Label(frame, text="Grade:").grid(row=2, column=0)
    Label(frame, text=student['grades']).grid(row=2, column=1)

    # Display the window
    window.mainloop()


display_report_card(student)
