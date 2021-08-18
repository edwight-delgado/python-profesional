from datetime import datetime, date

print(datetime.utcnow())
time = date.today()

print(f'year: {time.year}')
print(f'month: {time.month}')
print(f'day: {time.day}')