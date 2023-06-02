from student_data import student_registry
from teacher_data import teacher_list


constant_students = [
    {
        "first_name": "Adam",
        "last_name": "Watson",
        "sex": "Male",
        "DOB": "04/20/1969",
        "schedule": ["English Literature", "Biology", "Chemistry", "Computer Science", "Calculus", "Physics"],
        "grades": ["A", "A", "B+", "A", "A-", "B+"],
        "active": True
    },
    {
        "first_name": "Eilman",
        "last_name": "Karim",
        "sex": "Male",
        "DOB": "01/27/2004",
        "schedule": ["Physical Education", "Botany", "Gender Studies", "Pilates", "Buisness", "Physics"],
        "grades": ["C", "C-", "D", "A+", "C-", "L"],
        "active": True
    }
]

constant_teacher = [
    {
        "username": "tekadrad",
        "password": "radhika123",
        "first_name": "Radhika",
        "last_name": "Tekade",
        "subject": "Computer Science",
        "permissions": "teacher"
    },
]

admin = [
    {
        "username": "sharmdee",
        "password": "deepak123",
        "first_name": "Deepak",
        "last_name": "Sharma",
        "permissions": "admin"
    },
]


def combine_lists(parent, child):
    for i in child:
        parent.append(i)
    return (parent)


student_registry = combine_lists(student_registry, constant_students)
teacher_list = combine_lists(teacher_list, constant_teacher)
admin = admin


print(student_registry, teacher_list, admin)
