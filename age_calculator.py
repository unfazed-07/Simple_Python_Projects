from datetime import datetime
from dateutil.relativedelta import relativedelta

date_str = input("Enter a date in DD-MM-YYYY format: ")  # string input
date_obj = datetime.strptime(date_str, "%d%m%Y")

print("Converted datetime object:", date_obj.strftime("%d-%m-%Y"))
#print("Year:", date_obj.date, date_obj.month ,date_obj.year)
today=datetime.now()
print(today)

change=relativedelta(today,date_obj)

print(f"You are {change.years} years, {change.months} months and {change.days} days old")