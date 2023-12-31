import json

# Load the data from JSON files
with open('to_do.json', 'r') as file:
    to_do_data = json.load(file)

with open('base.json', 'r') as file:
    base_data = json.load(file)

with open('history.json', 'r') as file:
    history = json.load(file)

# Create the master dictionary
master_data = {}
for task in set(to_do_data.keys()).union(base_data.keys()):
    if task != "date":  # Exclude the 'date' key
        master_data[task] = {
            "current_value": to_do_data.get(task, None),
            "base_value": base_data.get(task, None),
            "history": history.get(task, None),
            "category": ""
        }

# Save the master data to a new file
with open('master.json', 'w') as file:
    json.dump(master_data, file, indent=4)

print("Master file created successfully.")
