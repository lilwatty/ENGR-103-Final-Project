import random

from common_functions import *

from raw_data import girls_names, boys_names, surnames, classes


def teacher_assignment():

    teacher_data = []

    for i in range(len(classes)):
        sex = assign_sex()
        first_name = generate_first_name(sex, boys_names, girls_names)
        last_name = generate_surname(surnames)
        teacher = {
            "username": generate_username(first_name, last_name),
            "password": generate_password(),
            "first_name": first_name,
            "last_name": last_name,
            "subject": assign_subject(),
            "permissions": "teacher"
        }
        teacher_data.append(teacher)

    return teacher_data


available_classes = classes.copy()


def assign_subject():
    subject = random.choice(available_classes)
    available_classes.remove(subject)
    return (subject)


def generate_username(first, last):

    last_name = split_string(last)
    first_name = split_string(first)

    if len(last) < 5:
        iterations = len(last)
    else:
        iterations = 5

    short_last = add_letter(iterations, last_name)
    short_first = add_letter(3, first_name)

    return combine_letter(short_last + short_first)


def add_letter(iterations, list):
    product = []
    for i in range(iterations):
        product.append(list[i])
    return product


def combine_letter(list):
    final = ""
    for i in list:
        final += str(i)
    return final


def split_string(string):
    list = []
    string = str(string).lower()
    for i in string:
        list.append(i)
    return (list)


def generate_password():
    password = ''
    for i in range(6):
        password += str(random.randint(0, 9))
    return password


# teacher_list = teacher_assignment()
