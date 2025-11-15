"""Functions for calculating currency exchange."""

def exchange_money(budget, exchange_rate):
    #Value after exchange
    return budget / exchange_rate
    
def get_change(budget, exchanging_value):
    #Currency after an exchange
    return budget - exchanging_value
    
def get_value_of_bills(denomination, number_of_bills):
    #Value of bills
    return denomination * number_of_bills
    
def get_number_of_bills(amount, denomination):
    #Number of bills (rounded)
    return amount // denomination
    
def get_leftover_of_bills(amount, denomination):
    #Leftover after exchanging into bills
    return amount % denomination
    
def exchangeable_value(budget, exchange_rate, spread, denomination):
    #Calculate value after exchange
    return (
        int(budget / (spread / 100 * exchange_rate + exchange_rate) / denomination) *denomination
    )