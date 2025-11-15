from datetime import datetime, timedelta

def delivery_date(start, description):
    start = datetime.strptime(start, "%Y-%m-%dT%H:%M:%S")
    if description == "NOW":
        start += timedelta(hours=2)
    elif description == "ASAP":
        set_hour = 17 if start.hour < 12 else 13
        if start.hour >= 12: start += timedelta(days=1)
        start = start.replace(hour=set_hour, minute=0, second=0)
    elif description == "EOW":
        if (W:=start.weekday()) > 4: raise ValueError("EOW input can't be on weekend")
        H = 17 if start.weekday() < 3 else 20 # set H=hour
        D = 4 if start.weekday() < 3 else 6 # set D=day
        start = start.replace(hour=H, minute=0, second=0) + timedelta(days=D - W)
    elif "M" in description:
        # set target month
        M = int(description.replace("M", ""))
        # set target year, +1 if start.month is after M(target month)
        Y = start.year + (M <= start.month)

        start = start.replace(year=Y, month=M, day=1, hour=8, minute=0, second=0)
        while start.weekday() > 4: start += timedelta(days=1)
    elif "Q" in description:
        quarters = ("1,2,3", "4,5,6", "7,8,9", "10,11,12")

        start_qtr = next(i+1 for i,q in enumerate(quarters) if str(start.month) in q)
        target_qtr = int(description.replace("Q", ""))

        # Y = start year + 1 if start quarter is after target quarter, else 0
        Y = start.year + (target_qtr < start_qtr)

        # M = int(str( last month of the target quarter ))
        M = int(quarters[target_qtr - 1][-2:].replace(",", ""))

        # D = last day of the target quarter
        D = (start.replace(month=M % 12 + 1, day=1) - timedelta(days=1)).day

        start = start.replace(year=Y, month=M, day=D, hour=8, minute=0, second=0)
        while start.weekday() > 4: start -= timedelta(days=1)

    start = datetime.strftime(start, "%Y-%m-%dT%H:%M:%S")
    return start