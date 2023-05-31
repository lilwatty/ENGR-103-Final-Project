import random

def generate_id():
    for i in range(9):
        id1 = "934"
        id2 = str(random.randint(100000,999999))
        id = id1 + id2
        return id
    
id = generate_id()
