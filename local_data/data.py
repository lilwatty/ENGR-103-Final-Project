import json


def convert_json_to_list(text_file):

    with open(text_file) as file:
        json_data = file.read()

    data_list = json.loads(json_data)
    return data_list


staff_registry = convert_json_to_list("local_data/employee_lists.txt")
student_registry = convert_json_to_list("local_data/student_files.txt")
