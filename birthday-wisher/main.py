##################### Extra Hard Starting Project ######################
import pandas
from random import randint
import datetime as dt
import smtplib

# 1. Update the birthdays.csv
birthdays = pandas.DataFrame({'name': ['Dan','Mum','Dad'],
             'email': ['tp_addr1','to_addr2', 'to_addr3'],
             'year':[1997,1958,1948],
             'month': [3,4,11],
             'day': [10,19,2]})
birthdays.to_csv('birthdays.csv',index= False)


# 2. Check if today matches a birthday in the birthdays.csv
today_date = dt.datetime.now()
today_month = today_date.month
today_day = today_date.day

check_birthday_list = pandas.read_csv('birthdays.csv')
birthday_list = check_birthday_list.to_dict(orient='records')




for birthday_boy in birthday_list:
    name = birthday_boy['name']
    birth_month = birthday_boy['month']
    birth_day = birthday_boy['day']
    to_address = birthday_boy['email']

    if birth_month == today_month and birth_day == today_day:
        random_letter = randint(1,3)
        with open(f'letter_templates/letter_{random_letter}.txt') as letter:
            changed_letter = "".join(letter.readlines()).replace('[NAME]', name)

        my_email = 'FROM_EMAIL'
        my_password = 'PASSWORD'

        with smtplib.SMTP('smtp.gmail.com') as connection:
            connection.starttls()
            connection.login(user=my_email,password=my_password)
            connection.sendmail(from_addr=my_email,
                                to_addrs=to_address,
                                msg=f'Subject: Happy Birthday \n\n {changed_letter}')







# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.




