import re

def load_csv(path: str) -> list[str]:
    try:
        with open(path, 'r') as f:
            data = f.readlines()
        return data
    except FileNotFoundError:
        print('file not found')
    except PermissionError:
        print('no access permission for file')

def remove_non_entries(data: list[str]) -> list[str]:
    return [line for line in data if re.search('[a-zA-Z]', line) is not None]

def remove_empty_fields(data: list[str]) -> list[str]:
    return [field.replace('\n', '') for field in data if len(field.strip()) != 0]

def validate_exact_match(string: str, pattern: str) -> bool:
    return bool(re.fullmatch(pattern, string))

def validate_id(string: str) -> bool:
    return validate_exact_match(string, r'^\d+$|^nan$')

def validate_name(string: str) -> bool:
    return validate_exact_match(string, r'^[a-zA-Z ]+$')

def validate_email(string: str) -> bool:
    return validate_exact_match(string, r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$')

def validate_amount(string: str) -> bool:
    return validate_exact_match(string, r'^[-+]?[0-9]*\.?[0-9]+$')

def sanitize_customer_data(customer_data: str) -> dict:
    customer_data = customer_data.split(',')
    customer_data = remove_empty_fields(customer_data)
    customer_data = [field.strip() for field in customer_data]

    customer_dict = {}

    for idx, field in enumerate(customer_data):
        if idx == 0 and 'id' not in customer_dict and validate_id(field):
            customer_dict['id'] = field
        elif idx < 2 and 'name' not in customer_dict and validate_name(field):
            customer_dict['name'] = field
        elif idx < 3 and 'email' not in customer_dict and validate_email(field):
            customer_dict['email'] = field
        elif validate_amount(field):
            customer_dict['amount'] = field

    for field in ['id', 'name', 'email', 'amount']:
        if field not in customer_dict:
            customer_dict[field] = 'none'

    return customer_dict

def save_data(data, path):
    try:
        with open(path, 'w') as f:
            f.write('customer_id, name, email, purchase_amount\n')
            for customer in data:
                f.write(f'{customer["id"]},{customer["name"]},{customer["email"]},{customer["amount"]}\n')
    except FileNotFoundError:
        print('Destination file not found')
    except PermissionError:
        print('You do not have permission to write to destination file')

        
data = load_csv('delopgave3/data/source_data.csv')

if data != None:
    data = remove_non_entries(data)
    data = [sanitize_customer_data(customer) for customer in data]
    save_data(data, 'delopgave3/data/sanitized_data.csv')
