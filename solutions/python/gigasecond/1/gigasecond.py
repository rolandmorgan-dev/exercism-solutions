from datetime import datetime
from datetime import timedelta

# Determining the date and time one gigasecond after a certain date.
def add(date_time : datetime) -> datetime:
    one_gigasecond = timedelta(seconds = 1000_000_000)
    gigasecond_later = date_time + one_gigasecond
    return gigasecond_later