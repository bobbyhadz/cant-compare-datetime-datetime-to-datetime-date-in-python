# TypeError: can't compare datetime.datetime to datetime.date

from datetime import datetime, date


dt = datetime(2024, 3, 15, 12, 0, 0)

print(dt)  # 👉️ 2024-03-15 12:00:00

d = date(2024, 2, 10)
print(d)  # 👉️ 2024-02-10

# ✅ Convert to date object
if d < datetime.date(dt):
    print('d is less than dt')
elif d > dt:
    print('d is greater than dt')
else:
    print('d is equal to dt')