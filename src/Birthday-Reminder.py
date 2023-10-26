import requests
from datetime import datetime, timedelta

def main():
    slack_webhook_url = "WEBHOOKURLHERE"

    with open('birthdays.txt', 'r') as file:
        data = file.readlines()

    today = datetime.now()

    for line in data:
        name, birthday = line.strip().split('--')
        birth_date = datetime(today.year, int(birthday.split('-')[0]), int(birthday.split('-')[1]))
        
        days_until_birthday = (birth_date - today).days+1

        if days_until_birthday in [2, 1, 0]:
            formatted_birthday = birth_date.strftime("%d %B")
            if days_until_birthday == 0:
                message = f"🎂 Reminder: Wish Happy Birthday to {name}! 🎉"
            else:
                message = f"🎉 Reminder: {name}'s birthday is in {days_until_birthday} days on {formatted_birthday}! 🎈"
    payload = {'text': message}
    requests.post(slack_webhook_url, json=payload)

if __name__ == "__main__":
    main()
 