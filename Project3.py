#Festival Reminder Bot....

from datetime import datetime, timedelta
import time
import json
from plyer import notification

def load_festivals():
    try:
        with open("festivals.json", "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return {}

def save_festivals(festivals):
    with open("festivals.json", "w") as f:
        json.dump(festivals, f, indent=4)

def send_notification(name, date, days_left):
    message = f"{name} is coming in {days_left} day(s) on {date}!"
    notification.notify(
        title="🎉 Festival Reminder",
        message=message,
        timeout=10
    )

def check_upcoming_festivals(festivals):
    today = datetime.now().date()
    for name, date_str in festivals.items():
        try:
            festival_date = datetime.strptime(date_str, "%Y-%m-%d").date()
            days_left = (festival_date - today).days
            if 0 <= days_left <= 3:
                send_notification(name, festival_date, days_left)
        except ValueError:
            print(f"Invalid date format for {name}: {date_str}")

def add_or_edit_festival(festivals):
    name = input("Enter festival name: ")
    date = input("Enter date (YYYY-MM-DD): ")
    try:
        datetime.strptime(date, "%Y-%m-%d")
        festivals[name] = date
        save_festivals(festivals)
        print(f"Festival '{name}' added/updated successfully.")
    except ValueError:
        print("Invalid date format. Please use YYYY-MM-DD.")

def main():
    festivals = load_festivals()
    check_upcoming_festivals(festivals)
    print("Checked for festival reminders. Sleeping for 24 hours...")
    time.sleep(3)

        
if __name__ == "__main__":
    while True:
        print("\n📅 Festival Reminder Bot")
        print("1. View Festivals")
        print("2. Add/Edit Festival")
        print("3. Start Daily Reminder")
        print("4. Exit")

        choice = input("Enter your choice: ").strip()
        festivals = load_festivals()

        if choice == "1":
            if festivals:
                print("\nUpcoming Festivals:")
                for fest, date in festivals.items():
                    print(f" - {fest}: {date}")
            else:
                print("No festivals found.")
        elif choice == "2":
            add_or_edit_festival(festivals)
        elif choice == "3":
            print("Starting the Festival Reminder Bot (daily checks)...")
            main()
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please select 1–4.")
