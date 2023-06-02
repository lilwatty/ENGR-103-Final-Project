from data.data_file import student_registry
from data.data_file import teacher_list
from data.data_file import admin

from .student_search import student_search


def main():
    student_search()


main()
print(student_registry, teacher_list, admin)
