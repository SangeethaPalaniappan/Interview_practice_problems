# Enumeration

from enum import Enum

class Weekday(Enum):
    Monday = 0
    Tuesday = 1
    Wednesday = 2
    Thursday = 3
    Friday = 4
    Saturday = 5
    Sunday = 6

today = Weekday.Wednesday
print(today)
if today == Weekday.Wednesday:
    print("It's Wednesday!")
else:
    print("It's not Wednesday.")

