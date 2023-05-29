import random
import datetime


girls_names = [
    'Emma', 'Olivia', 'Ava', 'Isabella', 'Sophia', 'Mia', 'Charlotte', 'Amelia',
    'Harper', 'Evelyn', 'Abigail', 'Emily', 'Elizabeth', 'Mila', 'Ella', 'Avery',
    'Sofia', 'Camila', 'Aria', 'Scarlett'
]

boys_names = [
    'Liam', 'Noah', 'William', 'James', 'Oliver', 'Benjamin', 'Elijah', 'Lucas',
    'Henry', 'Alexander', 'Sebastian', 'Jack', 'Aiden', 'Owen', 'Caleb', 'Andrew',
    'Daniel', 'Matthew', 'Joseph', 'Levi'
]

surnames = [
    'Smith', 'Johnson', 'Williams', 'Jones', 'Brown', 'Davis', 'Miller', 'Wilson',
    'Moore', 'Taylor', 'Anderson', 'Thomas', 'Jackson', 'White', 'Harris', 'Martin',
    'Thompson', 'Garcia', 'Martinez', 'Robinson', 'Clark', 'Rodriguez', 'Lewis',
    'Lee', 'Walker', 'Hall', 'Allen', 'Young', 'Hernandez', 'King', 'Wright',
    'Lopez', 'Hill', 'Scott', 'Green', 'Adams', 'Baker', 'Gonzalez', 'Nelson',
    'Carter', 'Mitchell', 'Perez', 'Roberts', 'Turner', 'Phillips', 'Campbell',
    'Parker', 'Evans', 'Edwards', 'Collins', 'Stewart', 'Sanchez', 'Morris', 'Rogers',
    'Reed', 'Cook', 'Morgan', 'Bell'
]


def generate_sample_student_data(enrollment):
    sample_student_data = []
    for i in range(enrollment):
        sex = assign_sex()
        student = {
            "sex": sex,
            "first_name": generate_first_name(sex),
            "last_name": generate_surname(),
            "DOB": assign_DOB()
        }
        sample_student_data.append(student)
    print(sample_student_data)


"""
"ID": generate_ID(),
"schedule": generate_schedule(),
"grades": auto_grader()
"""


def assign_sex():
    odds = random.random()
    if odds <= .55:
        sex = "Male"
    else:
        sex = "Female"
    return sex


def generate_first_name(sex):
    if sex == "Male":
        first_name = random.choice(boys_names)
    else:
        first_name = random.choice(girls_names)
    return first_name


def generate_surname():
    return random.choice(surnames)


def day_month_match(month):

    if month == 2:
        day = random.randint(1, 28)
    elif month == 4 or month == 6 or month == 9 or month == 11:
        day = random.randint(1, 30)
    else:
        day = random.randint(1, 31)

    return day


def assign_DOB():

    month = random.randint(1, 12)
    day = day_month_match(month)
    year = random.randint(2000, 2005)

    dob = datetime.datetime(year, month, day)
    dob = dob.strftime("%m/%d/%Y")
    return (dob)


generate_sample_student_data(1)
