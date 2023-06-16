import random
from local_data.data import student_registry


def unique_id_checker(created):
    for i in student_registry:
        id = i["ID"]
        if created == id:
            generate_id()
        else:
            return created


def generate_id():
    num_set1 = str(random.randint(100, 999))
    num_set2 = str(random.randint(100, 999))
    id = "934-" + num_set1 + "-" + num_set2

    unique_id = unique_id_checker(id)
    return unique_id


id = generate_id()
