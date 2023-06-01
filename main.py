import datetime as dt
import pandas
import random
import smtplib


EMAIL = "learnerpython97@gmail.com"
PASSWORD = "password"
# need to use APP password from google account in place of password

now = dt.datetime.now()

today = (now.month,now.day)
print(today)

data = pandas.read_csv("birthdays.csv")

birthday_dict = {(data_row["month"],data_row["day"]):data_row for (index,data_row) in data.iterrows()}

print(birthday_dict)

if today in birthday_dict:
    birthday_person = birthday_dict[today]
    with open(f"letter_templates/letter_{random.randint(1,3)}.txt   ") as letter:
        contents = letter.read()
        birtdhay_letter = contents.replace("[NAME]",birthday_person["name"])

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(EMAIL,PASSWORD)
        connection.sendmail(from_addr=EMAIL,
                            to_addrs=birthday_person["email"],
                            msg=f"subject: Happy birthday!!!\n\n{birtdhay_letter}"
                            )
