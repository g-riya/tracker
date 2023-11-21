from datetime import date
import json


file_path = 'to_do.json'

with open(file_path, 'r') as file:
    loaded_dict = json.load(file)

file_path = 'base.json'

with open(file_path, 'r') as file:
    base_data = json.load(file)

def save_data(data, file_path):
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)


while True:
    user_input = input("Enter prompt (or 'exit' to stop): ").lower()
    num_days = int(input("Enter num of days"))
    if user_input == 'exit':
        break

    # Process the input (in this example, we're just storing the input as-is)
    loaded_dict[user_input] = num_days
    base_data[user_input] = num_days

    # Save the updated data to the JSON file
    save_data(loaded_dict, "to_do.json")
    save_data(base_data, "base.json")