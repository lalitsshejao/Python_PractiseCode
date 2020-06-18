import datetime
import time
today=datetime.date.today()

print(today)

birthday = datetime.date(1981, 9, 17)
print(birthday)

days_since_birth = (today-birthday).days
print (days_since_birth)

tdate= datetime.timedelta(days=10)
print(today + tdate)

print(today.day)
print(today.weekday())
# Monday =0 Sunday = 6

# datetime.date   (Y, M, D)
# datetime.time   (h,m,s,ms)
# datetime.datetime    (Y, M, D, h,m,s,ms)

hour_delta = datetime.timedelta(hours = 10)
print(datetime.datetime.now() + hour_delta)

print (time.time())
print (time.ctime(time.time()))

print(time.localtime())
a= time.localtime()
b = time.mktime(a)
c = time.asctime(a)
print(b)
print(c)

help(time.strftime)
x= time.strftime("%m/%d/%Y")
print(x)
y= time.strftime("%B/%d/%Y")
print(y)