import datetime
print(datetime.datetime.now())
tday = datetime.date.today()
print(tday.weekday())
# print(tday.isoweekday())

# time delta
tdelta = datetime.timedelta(days=7)
print(tday + tdelta)

# date2 = date1 + timedelta
# timedelta = date1 + date2

bday = datetime.date(2018, 6, 9)
till_bday = bday - tday
print(till_bday)

t = datetime.datetime.now()  # .today() .utcnow()
print(t)
print(t.time())
