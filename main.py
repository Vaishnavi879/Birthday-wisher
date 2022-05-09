import smtplib
import datetime as dt
import random
today_quote=""

def send_mail(quote):
    my_email="timmyturtle43@yahoo.com"
    my_password="kywqhgyaxrgsvfgr"

    with smtplib.SMTP("smtp.mail.yahoo.com",587) as connection:
        connection.starttls()
        connection.login(user=my_email,password=my_password)
        connection.sendmail(from_addr=my_email,to_addrs=my_email,msg=f"Subject:Today's quote\n\n{quote}")


now=dt.datetime.now()
year=now.year
month=now.month
day_of_week=now.weekday()

date_of_birth=dt.datetime(year=2002,month=10,day=29)

if day_of_week==4:
    random_number=random.randint(0,100)
    with open("quotes.txt","r") as file:
        data=file.readlines()
        today_quote=data[random_number]
        send_mail(today_quote)
