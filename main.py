import smtplib
import datetime as dt
import random

my_email = "jfrancone.automail@gmail.com"
port1_SSL = 465
with open ("pw.txt") as file:
    password = file.readline()

now = dt.datetime.now()
day_of_week = now.weekday()

with open("quotes.txt") as file:
    contents = file.readlines()

#print(contents)
#print(type(contents))

todays_quote = random.choice(contents)

#print(todays_quote)

Subject = "Motivational Quote"
Content = todays_quote

if day_of_week == 5:
    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as connection:
        connection.login(user = my_email, password = password)
        #connection.login(user = my_email, password = password)
        connection.sendmail(from_addr=my_email, to_addrs="jfrancone.automail@yahoo.com", msg =f"Subject: {Subject} \n\n{Content}")