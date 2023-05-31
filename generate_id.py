import random

def generate_id():
    randnums = str(random.randint(100000,999999))
    id = "934" + randnums
    return id
    
id = generate_id()
