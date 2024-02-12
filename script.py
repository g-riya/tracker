from datetime import date, datetime, timedelta
import json

birthdays = 'birthdays.json'
master = 'master.json'

with open(master, 'r') as file:
    master_dict = json.load(file)

with open(birthdays, 'r') as file:
    birthdays_data = json.load(file)

def save_data(data, file_path):
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)

today = datetime.today()  # Include the time information
if today.hour < 4:
    today -= timedelta(days=1)
original_date = datetime.strptime(master_dict["date"], '%Y-%m-%d')
current_year = date.today().year

def log():
    user_input = input("Enter prompt or EXIT to exit: ").lower()
    while (user_input != "exit"):
        if user_input in master_dict:
            master_dict[user_input]["current_value"] = master_dict[user_input]["base_value"]
            master_dict[user_input]["history"].append(date.today().strftime("%Y-%m-%d"))
            save_data(master_dict, "master.json")
        else:
            print(f"Task '{user_input}' not found. Please enter a valid task.")
        user_input = input("Enter prompt or EXIT to exit: ").lower()

def retro():
    user_input = input("Enter prompt or EXIT to exit: ").lower()
    while (user_input != "exit"):
        if user_input in master_dict:
            days_prev = int(input("Enter how many days prev: "))
            master_dict[user_input]["current_value"] = master_dict[user_input]["base_value"] - days_prev
            master_dict[user_input]["history"].append((date.today() - timedelta(days=days_prev)).strftime("%Y-%m-%d"))
            save_data(master_dict, "master.json")
        else:
            print(f"Task '{user_input}' not found. Please enter a valid task.")

        user_input = input("Enter prompt or EXIT to exit: ").lower()

def todo():
    days_since = (today-original_date).days
    master_dict["date"] = date.today().strftime("%Y-%m-%d")
    tasks_by_category = {}

    for key, value in master_dict.items():
        if key != "date" and master_dict[key]["base_value"] != "inactive":
            category = value.get("category", "Other")
            if category == "":
                category = "Other"
            master_dict[key]["current_value"] -= days_since
            if master_dict[key]["current_value"] <= 0:
                if category not in tasks_by_category:
                    tasks_by_category[category] = []
                tasks_by_category[category].append(key)

    for category, tasks in tasks_by_category.items():
        print(f"{category}:")
        for task in tasks:
            print(f" - {task}")
        print()

    save_data(master_dict, "master.json")

    for name, cur_bday in birthdays_data.items():
        month, day = map(int, cur_bday.split('-'))
        bday_date_this_year = date(current_year, month, day)
        bday_date_next_year = date(current_year + 1, month, day)

        if bday_date_this_year >= date.today():
            days_until_bday = (bday_date_this_year - date.today()).days
        else:
            days_until_bday = (bday_date_next_year - date.today()).days

        if 0 <= days_until_bday <= 15:
            if days_until_bday == 0:
                print(f"It's {name}'s birthday today!")
            else:
                print(f"It's {name}'s birthday in {days_until_bday} days!")

def add():
    user_input = input("Enter prompt: ").lower()
    num_days = int(input("Enter num of days: "))
    category = input("Enter category: ")
    if user_input not in master_dict:
        master_dict[user_input] = {
            "current_value": num_days,
            "base_value": num_days,
            "history": [],  
            "category": category
        }
    else:
        master_dict[user_input]["current_value"] = num_days
        master_dict[user_input]["base_value"] = num_days
    save_data(master_dict, "master.json")

# say all that are deactive, all that are active, 
def deactivate():
    user_input = input("Enter prompt or EXIT to exit: ").lower()
    while (user_input != "exit"):
        if user_input in master_dict:
            master_dict[user_input]["base_value"] = "inactive"
            save_data(master_dict, "master.json")
        else:
            print(f"Task '{user_input}' not found. Please enter a valid task.")
        user_input = input("Enter prompt or EXIT to exit: ").lower()


while True:
    command = input("Would you like to LOG, RETRO LOG, DEACTIVATE, see what TODO, ADD or EXIT?: ").lower()
    if command == "exit":
        exit()
    elif command == "log":
        log()
    elif command == "retro log":
        retro()
    elif command == "deactivate":
        deactivate()
    elif command == "todo":
        todo()
    elif command == "add":
        add()
    else:
        print("Not a valid command")
