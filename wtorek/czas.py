import calendar as c
import time
from datetime import date

import arrow as arrow

print(c.calendar(1900))
print(c.month(2020, 11))
print(c.weekday(2022, 12, 18))

local_time = time.ctime()
print(local_time)
# time.sleep(5)
local_time2 = time.ctime()
print(local_time2)
czas = time.localtime()

time_string = time.strftime("%d-%m-%Y  %H:%M", czas)
print(time_string)

print(arrow.utcnow())
print(arrow.now())
print(arrow.now('Pacific/Pago_Pago'))

dzis = date.today()
print(dzis.day)
print(dzis.month)
print(dzis.year)

