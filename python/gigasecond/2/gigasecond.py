from datetime import datetime, timedelta

# Determining the date and time one gigasecond after a certain date.
def add(t : datetime) -> datetime:
    return t + timedelta(seconds = 1e9)