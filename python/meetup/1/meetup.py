from datetime import date
import calendar

# Occurrences of a day
TXT_NUM = {"first":1, "second":2, "third":3, "fourth":4, "fifth":5,"teenth":1, "last":1}

class MeetupDayException(ValueError):
    def __init__(self, message):
        super().__init__(message)

def meetup(year: int, month: int, week: str, day_of_week: str) -> date:
    # Days in the given month
    _, max_days = calendar.monthrange(year, month)
    
    # List of day names in the month
    days = [date(year,month,day).strftime('%A') for day in range(1, max_days+1)]
    
    # Validate input and check if the day exists
    if week not in TXT_NUM or days.count(day_of_week) < TXT_NUM[week]:
        raise MeetupDayException("That day does not exist.")
    
    if week == "teenth":
        return date(year, month, 13+(days[12:19].index(day_of_week)))
    
    if week == "last":
        return date(year, month, max_days-(days[::-1].index(day_of_week)))
    
    # Handle the nth occurrence: first, second, third, fourth, or fifth
    day = tuple(i+1 for i, d in enumerate(days) if d == day_of_week)[TXT_NUM[week]-1]
    
    return date(year, month, day)