from login import login
from student_search import search_student

from local_data.data import staff_registry, student_registry

sample_data = [
    {
        "username": "123",
        "password": "123",
        "first_name": "Daniel",
        "last_name": "Perez",
        "subject": "Statistics",
        "permissions": "teacher"
    },
]


for i in sample_data:
    staff_registry.append(i)


def main():
    user_data = login(staff_registry)
    search_student(user_data, student_registry)


main()
