# To get the current date and time, we need the datetime library.
from datetime import datetime
from datetime import timedelta
# OR

# from datetime import datetime, timedelta

current_date = datetime.now()
print(current_date)

print("-"* 40)

# timedelta is used to define a period of time; it is found in the datetime library.
one_day = timedelta(days=1)
yesterday = current_date - one_day
print("Yesterday was: " + str(yesterday))

from datetime import date
print("Day: "+ str(current_date.day))
print("Month: " + str(current_date.month))
print("Year: " + str(current_date.year))

print("-"* 40)

# To convert a sate string to a datetime object:
birthday = input("When is your birthday (dd/mm/yyyy)? ")
birth_date = datetime.strptime(birthday, "%d/%m/%Y")

print("Birthday is " + str(birth_date))

print("-"* 40)

a_day_before = timedelta(days=1)
birthday_eve = birth_date - a_day_before

print("A Day Before your Birthday is " + str(birthday_eve))