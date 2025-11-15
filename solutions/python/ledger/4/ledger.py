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
    money = "{:,.2f}".format(amount / 100)
    if is_dutch: money = money.replace(".", "X").replace(",", ".").replace("X", ",")
    b = ("(",")") if is_negative else (""," ")
    return f"{sign} {money} " if is_dutch else f"{b[0]}{sign}{money}{b[1]}"

def format_entries(currency, locale_name, entries):
    title_lang = {"en_US":("Date","Description","Change"),
                  "nl_NL":("Datum","Omschrijving","Verandering")}
    
    if locale_name == "nl_NL": date_type = "%d-%m-%Y"
    else: date_type = "%m/%d/%Y"
    
    str_Date, str_Desc, str_Change = title_lang[locale_name]
    board = ["{:<10} | {:<25} | {:<13}".format(str_Date, str_Desc, str_Change)]
    
    sorted_entries = sorted(entries, key=lambda e: (e.date, e.desc, e.change))
    for entry in sorted_entries:
        date = datetime.strftime(entry.date, date_type)
        change = format_money(currency, entry.change, locale_name)
        desc = entry.desc[:22] + "..." if len(entry.desc) >= 25 else entry.desc
        board.append("{:<10.10} | {:<25} | {:>13.13}".format(date, desc, change))
    
    return "\n".join(board)