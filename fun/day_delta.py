from datetime import date, timedelta, datetime

st = date(2025, 3, 29)
en = date(2025, 6, 6)
print(en - st)

today = datetime.now().date()
birthday = date(1988, 9, 2)

dlt = today - birthday

print(dlt.total_seconds())
print(dlt.total_seconds() // 60)
print(dlt.total_seconds() // 3600)
print(dlt.total_seconds() // (3600 * 24))
print(dlt.days)
print(dlt.days // 365 )
x = 2 * (10 ** 7)
y = 333333
a = timedelta(minutes=x)
print(birthday + a)  #  2026-09-11
b = timedelta(hours=y)
print(birthday + b)
print(x / y)
z = 1234567890
c = timedelta(seconds=z)
print(birthday + c)
