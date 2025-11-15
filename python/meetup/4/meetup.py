from calendar import monthrange
from datetime import date

ORD = {"first":1, "second":2, "third":3, "fourth":4, "fifth":5}
WEEKS = {*ORD, "teenth", "last"}

class MeetupDayException(Exception): pass

def meetup(year: int, month: int, week: str, weekday: str) -> date:
    _, m_days = monthrange(year, month)
    days = [date(year,month,day).strftime("%A") for day in range(1, m_days+1)]
    
    checks = (("week", week not in WEEKS),
              ("day of the week", weekday not in days),
              ("day", days.count(weekday) < ORD.get(week,1)))
    
    if (errors := tuple(label for label, failed in checks if failed)):
        raise MeetupDayException(f"That {' and '.join(errors)} does not exist.")
    
    if week == "teenth":
        return date(year, month, 13+(days[12:19].index(weekday)))
    
    if week == "last":
        return date(year, month, m_days-(days[::-1].index(weekday)))
    
    day = tuple(i+1 for i, d in enumerate(days) if d == weekday)[ORD[week]-1]
    
    return date(year, month, day)