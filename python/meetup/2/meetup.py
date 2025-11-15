from calendar import monthrange, day_name
from datetime import date

ORD = {"first":1, "second":2, "third":3, "fourth":4, "fifth":5}
WEEKS = {*ORD, "teenth", "last"}

class MeetupDayException(Exception): pass

def meetup(year: int, month: int, week: str, w_day: str) -> date:
    _, m_days = monthrange(year, month)
    days = [date(year,month,day).strftime("%A") for day in range(1, m_days+1)]
    
    if week not in WEEKS or w_day not in day_name or days.count(w_day) < ORD.get(week,1):
        raise MeetupDayException("That day does not exist.")
    
    if week == "teenth":
        return date(year, month, 13+(days[12:19].index(w_day)))
    
    if week == "last":
        return date(year, month, m_days-(days[::-1].index(w_day)))
    
    day = tuple(i+1 for i, d in enumerate(days) if d == w_day)[ORD[week]-1]
    
    return date(year, month, day)