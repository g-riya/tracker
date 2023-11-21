from datetime import date, datetime
import json


file_path = 'to_do.json'

with open(file_path, 'r') as file:
    loaded_dict = json.load(file)

today = datetime.today()

original_date = datetime.strptime(loaded_dict["date"], '%Y-%m-%d')

days_since = (today-original_date).days

for key in loaded_dict.keys():
    if key == "date":
        loaded_dict[key] =  date.today().strftime("%Y-%m-%d")
    else:
        loaded_dict[key] -= days_since
        if loaded_dict[key] < 0:
            print(f"{key}")

with open(file_path, 'w') as file:
    json.dump(loaded_dict, file, indent=4)
