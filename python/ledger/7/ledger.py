from datetime import datetime

def create_entry(date, desc, change):
    return (datetime.strptime(date, '%Y-%m-%d'), desc, change)

def format_money(currency, amount, locale):
    is_dutch = locale == "nl_NL"
    is_negative = amount < 0
    sign = "€" if currency == "EUR" else "$"
    money = "{:,.2f}".format((amount if is_dutch else abs(amount)) / 100)
    if is_dutch: money = money.replace(".", "X").replace(",", ".").replace("X", ",")
    wrap = ("(",")") if is_negative else (""," ")
    return f"{sign} {money} " if is_dutch else f"{wrap[0]}{sign}{money}{wrap[1]}"

def format_entries(currency, locale_name, entries):
    if locale_name == "nl_NL": header = "Datum", "Omschrijving", "Verandering"
    else: header = "Date", "Description", "Change"
    
    date_type = "%d-%m-%Y" if locale_name == "nl_NL" else "%m/%d/%Y"
    
    board = ["{:10} | {:25} | {:13}".format(*header)]
    
    # entry[0] -> Date, entry[1] -> Description, entry[2] -> Change
    for entry in sorted(entries, key=lambda entry: (entry[0], entry[2], entry[1])):
        date = datetime.strftime(entry[0], date_type)
        desc = entry[1][:22] + "..." if len(entry[1]) >= 25 else entry[1]
        change = format_money(currency, entry[2], locale_name)
        board.append("{:10.10} | {:25} | {:>13.13}".format(date, desc, change))
    
    return "\n".join(board)