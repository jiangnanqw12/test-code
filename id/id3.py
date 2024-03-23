import uuid
import json


def generate_id():
    return str(uuid.uuid4())[:8]


def record_data(new_id, file_type, description, filename='data.json'):
    new_record = {
        'id': new_id,
        'file_type': file_type,
        'description': description
    }

    try:
        with open(filename, 'r') as file:
            data = json.load(file)

    except FileNotFoundError:
        data = []

    if new_record not in data:
        data.append(new_record)
        with open(filename, 'w') as file:
            json.dump(data, file, indent=4)
        return True
    return False


# 示例
new_id = generate_id()
# new_id = "0c8d77ba"
if record_data(new_id, 'pdf', 'This is a PDF file'):
    print(f"New record with ID '{new_id}' has been recorded.")
else:
    print(f"Record with ID '{new_id}' already exists.")
