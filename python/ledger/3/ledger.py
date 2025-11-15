from datetime import datetime

class LedgerEntry:
    def __init__(self, date, description, change):
        self.date = datetime.strptime(date, "%Y-%m-%d").date()
        self.desc = description
        self.change = change

create_entry = LedgerEntry

def format_money(currency, amount, loc):
    is_dutch = loc == "nl_NL"
    is_negative = amount < 0
    amount = amount if is_dutch else abs(amount)
    sign = "€" if currency == "EUR" else "$"
    major_units = f"{int(amount / 100):,}"
    if is_dutch: major_units = major_units.replace(",", ".")
    minor_units = abs(amount - int(amount / 100) * 100)
    coma = "," if is_dutch else "."
    money = f"{major_units}{coma}{minor_units:02d}"
    b = ("(",")") if is_negative else (""," ")
    result = f"{sign} {money} " if is_dutch else f"{b[0]}{sign}{money}{b[1]}"
    return result

def format_entries(currency, locale_name, entries):
    title_lang = {"en_US":("Date","Description","Change"),
                  "nl_NL":("Datum","Omschrijving","Verandering")}
    
    if locale_name == "nl_NL": date_type = "%d-%m-%Y"
    else: date_type = "%m/%d/%Y"
    
    str_Date, str_Desc, str_Change = title_lang[locale_name]
    board = ["{:<10} | {:<25} | {:<13}".format(str_Date, str_Desc, str_Change)]
    
    for entry in sorted(entries, key=lambda e: (e.date, e.desc, e.change)):
        date = datetime.strftime(entry.date, date_type)
        change = format_money(currency, entry.change, locale_name)
        desc = entry.desc[:22] + "..." if len(entry.desc) >= 25 else entry.desc
        board.append("{:<10.10} | {:<25} | {:>13.13}".format(date, desc, change))
    
    return "\n".join(board)