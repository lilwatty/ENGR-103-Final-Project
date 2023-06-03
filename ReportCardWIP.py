from tkinter import Tk, Label, Frame
from local_data.data import student_registry
from login import user_data

"""
The get_student_by_id isn't necessary, this function will take in the entire dictionary of student information as the input.

"""


def display_report_card(student_id):
    # Get the student details from the student registry
    student = student_registry.get_student_by_id(student_id)

    # Create a Tkinter window
    window = Tk()
    window.title("Report Card")

    # Create a frame to hold the report card information
    frame = Frame(window)
    frame.pack()

    # Create labels to display the student's information
    Label(frame, text="Name:").grid(row=0, column=0)
    Label(frame, text=student.name).grid(row=0, column=1)

    Label(frame, text="ID:").grid(row=1, column=0)
    Label(frame, text=student.id).grid(row=1, column=1)

    Label(frame, text="Grade:").grid(row=2, column=0)
    Label(frame, text=student.grade).grid(row=2, column=1)

    # Display the window
    window.mainloop()


def main():
    student_id = input("Enter student ID: ")
    display_report_card(student_id)


if __name__ == "__main__":
    main()
