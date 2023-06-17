import json


def save_dict_list_to_json(list_of_dicts, file_path):
    # Convert list of dictionaries to JSON format
    json_data = json.dumps(list_of_dicts)

    # Save JSON data to a file
    with open(file_path, 'w') as file:
        file.write(json_data)
