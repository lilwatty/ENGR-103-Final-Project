import random
from local_data.data import student_registry

def generate_id():
    num_set1 = str(random.randint(100,999))
    num_set2 = str(random.randint(100, 999))     
    id = "934-" + num_set1 + "-" + num_set2
    for i in student_registry:
        if i["ID"] == id:
            generate_id()
    return id
      
id = generate_id()
