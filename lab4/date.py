import copy
from datetime import datetime, timedelta

a=datetime.now()

#1
b=a-timedelta(days=5)
print("Date 5 days ago:",b.strftime("%x"))
#2
print("Today:",a.strftime("%x"))
yesterday=a-timedelta(days=1)
print("Yesterday:",yesterday.strftime("%x"))
tomorrow=a+timedelta(days=1)
print("Tomorrow:",tomorrow.strftime("%x"))
#3
c=a.replace(microsecond=0)
print("Drop microseconds:",c)
#4
day1=int(input("day1:"))
month1=int(input("month1:"))
year1=int(input("year1:"))
date1=datetime(year1,month1,day1)
day2=int(input("day2:"))
month2=int(input("month2:"))
year2=int(input("year2:"))
date2=datetime(year2,month2,day2)
dif=date1-date2
print(dif.total_seconds())