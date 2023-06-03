import json

from student_data import student_registry
from teacher_data import teacher_list

from raw_data import constant_students
from raw_data import constant_teacher
from raw_data import admin


def combine_lists(primary, secondary):
    for i in secondary:
        primary.append(i)
    return primary


student_registry = combine_lists(student_registry, constant_students)
teacher_list = combine_lists(teacher_list, constant_teacher)
employee_list = combine_lists(teacher_list, admin)


def convert_to_json(list, filepath):
    with open(filepath, 'w') as file:
        json.dump(list, file, indent=4)


# convert_to_json(student_registry, "student_files.txt")
# convert_to_json(employee_list, "employ_lists.txt")
