# Function to check if a year is leap year. (in the Gregorian calendar)
def leap_year(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    return False

"""
import calendar

def leap_year(year):
    return True if calendar.isleap(year) else False
"""
