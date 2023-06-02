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

classes = [
    "English Literature",
    "Biology",
    "World History",
    "Computer Science",
    "Chemistry",
    "US History",
    "Physics",
    "Statistics",
    "Calculus",
    "Psychology",
]


def generate_sample_student_data(enrollment):
    sample_student_data = []
    for i in range(enrollment):
        sex = assign_sex()
        student = {
            "first_name": generate_first_name(sex),
            "last_name": generate_surname(),
            "sex": sex,
            "DOB": assign_DOB(),
            "schedule": generate_schedule(),
            "grades": generate_grade(),
            "active": student_status()
        }
        sample_student_data.append(student)
    return (sample_student_data)


"""
"ID": generate_ID(),

"""


def student_status():
    if random.random() >= .2:
        return True
    else:
        return False


def assign_sex():
    odds = random.random()
    if odds <= .534:
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


def generate_schedule():
    student_schedule = []
    i = 1
    max_length = 6
    while i <= max_length:
        new_class = random.choice(classes)
        if unique_list_check(new_class, student_schedule) == True:
            student_schedule.append(new_class)
            i += 1
        else:
            continue

    return student_schedule


def unique_list_check(item, list):
    if list.count(item) >= 1:
        return False
    else:
        return True


def generate_grade():
    grade_list = []
    potential = ['F', 'D', 'C', 'B', 'A']
    weights = [1, 2, 3, 2, 1]

    for i in range(6):
        grade = random.choices(potential, weights)[0]
        grade_list.append(grade)

    return (grade_list)


enrollment = 100

student_registry = generate_sample_student_data(enrollment)
