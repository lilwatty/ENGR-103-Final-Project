import random


def assign_sex():
    odds = random.random()
    if odds <= .534:
        sex = "Male"
    else:
        sex = "Female"
    return sex


def generate_first_name(sex, boy_options, girl_options):
    if sex == "Male":
        first_name = random.choice(boy_options)
    else:
        first_name = random.choice(girl_options)
    return first_name


def generate_surname(last_options):
    return random.choice(last_options)


def main():
    return assign_sex, generate_first_name, generate_surname


# main()
