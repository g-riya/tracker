from datetime import date, datetime, timedelta
import json

to_do = 'to_do.json'
base = 'base.json'
history = 'history.json'
birthdays = 'birthdays.json'


with open(to_do, 'r') as file:
    loaded_dict = json.load(file)

with open(base, 'r') as file:
    base_data = json.load(file)

with open(history, 'r') as file:
    history_data = json.load(file)

with open(birthdays, 'r') as file:
    birthdays_data = json.load(file)

def save_data(data, file_path):
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)

today = datetime.today()
original_date = datetime.strptime(loaded_dict["date"], '%Y-%m-%d')


while True:
    command = input("Would you like to LOG, see what TODO, ADD, HISTORY or EXIT?: ")
    if command == "EXIT":
        exit()
    elif command == "LOG":
        user_input = input("Enter prompt or EXIT to exit: ").lower()
        while (user_input != "exit"):
            loaded_dict[user_input] = base_data[user_input]
            save_data(loaded_dict, "to_do.json")
            history_data[user_input].append(date.today().strftime("%Y-%m-%d"))
            save_data(history_data, "history.json")
            user_input = input("Enter prompt or EXIT to exit: ").lower()
    elif command == "TODO":
        days_since = (today-original_date).days
        for key in loaded_dict.keys():
            if key == "date":
                loaded_dict[key] =  date.today().strftime("%Y-%m-%d")
            else:
                loaded_dict[key] -= days_since
                if loaded_dict[key] <= 0:
                    print(f"{key}")
        with open(to_do, 'w') as file:
            json.dump(loaded_dict, file, indent=4)
        day = loaded_dict["date"][-5:]
        day_15 = (date.today() + timedelta(days=15)).strftime("%m-%d")
        for name, cur_bday in birthdays_data.items():
            if cur_bday == day:
                print(f"its {name}'s birthday!")
            if cur_bday == day_15:
                print(f"its {name}'s birthday in 15 days!")
    elif command == "ADD":
        user_input = input("Enter prompt: ").lower()
        num_days = int(input("Enter num of days: "))
        loaded_dict[user_input] = num_days
        base_data[user_input] = num_days
        history_data[user_input] = []
        save_data(loaded_dict, "to_do.json")
        save_data(base_data, "base.json")
        save_data(history_data, "history.json")