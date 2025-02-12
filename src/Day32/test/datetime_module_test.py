import datetime as dt
import random

# now is a class
now = dt.datetime.now()
# year is an integer
year = now.year
month = now.month
day = now.day

day_of_week = now.weekday()

print(now)
print(year)
print(month)
print(day)
print(day_of_week)

date_of_birth = dt.datetime(
    year=random.randint(1990, 2000),
    month=random.randint(1, 12),
    day=26)

print(date_of_birth)

