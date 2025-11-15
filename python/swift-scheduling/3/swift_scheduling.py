from datetime import datetime, timedelta

# Calculates the delivery date and time from the meeting start and description.
def delivery_date(start: str, description: str) -> str:
    start = datetime.strptime(start, "%Y-%m-%dT%H:%M:%S")
    if description == "NOW":
        start += timedelta(hours=2)
    elif description == "ASAP":
        set_hour = 17 if start.hour < 12 else 13
        if start.hour >= 12: start += timedelta(days=1)
        start = start.replace(hour=set_hour, minute=0, second=0)
    elif description == "EOW":
        if (Wday:=start.weekday()) > 4: raise ValueError("EOW input can't be a weekend")
        H = 17 if Wday < 3 else 20
        D = 4 if Wday < 3 else 6
        start = start.replace(hour=H, minute=0, second=0) + timedelta(days=D - Wday)
    elif "M" in description:
        # set target month
        M = int(description[:-1])
        # set target year; add 1 if start.month is after target month
        Y = start.year + (M <= start.month)

        start = start.replace(year=Y, month=M, day=1, hour=8, minute=0, second=0)
        while start.weekday() > 4: start += timedelta(days=1)
    elif "Q" in description:
        quarters = ((1, 2, 3), (4, 5, 6), (7, 8, 9), (10, 11, 12))

        start_qtr = next(i+1 for i,q in enumerate(quarters) if start.month in q)
        target_qtr = int(description[-1:])

        # Y = start year + 1 if start quarter is after target quarter; else same year
        Y = start.year + (target_qtr < start_qtr)

        # M = last month of the target quarter
        M = quarters[target_qtr - 1][-1]

        # D = last day of the target quarter
        D = (start.replace(month=M % 12 + 1, day=1) - timedelta(days=1)).day

        start = start.replace(year=Y, month=M, day=D, hour=8, minute=0, second=0)
        while start.weekday() > 4: start -= timedelta(days=1)

    return datetime.strftime(start, "%Y-%m-%dT%H:%M:%S")