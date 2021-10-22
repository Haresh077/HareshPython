from datetime import date
from datetime import time
from datetime import datetime

today=date.today() #today date
print(today)
print(today.strftime("%Y")) # Print only year with yyyy format
print(today.strftime("%y")) # Print only year with yy format
print(today.strftime("%a")) # Print today week name
print(today.strftime("%d")) # Print today date dd format
print(today.strftime("%B")) # Print month name
print(today.strftime("%a,%d %B,%y")) # Print week,date,month,year
print(today.strftime("%x")) # print today date in mm/dd/yy format
