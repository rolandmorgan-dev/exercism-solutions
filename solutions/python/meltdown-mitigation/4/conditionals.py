#Reactor Control
def is_criticality_balanced(temperature, neutrons_emitted):
    if temperature < 800 and neutrons_emitted > 500 and (temperature * neutrons_emitted) < 500000:
        return True
    else:
        return False
        
def reactor_efficiency(voltage, current, theoretical_max_power):
    percentage_value = (voltage*current/theoretical_max_power)*100
    if percentage_value >= 80:
        c = "green"
    elif 60 <= percentage_value < 80:
        c = "orange"
    elif 30 <= percentage_value < 60:
        c = "red"
    else:
        c = "black"
    return c
    
def fail_safe(temperature, neutrons_produced_per_second, threshold):
    reactor_percentage = temperature * neutrons_produced_per_second/threshold*100
    if reactor_percentage < 90:
        return "LOW"
    elif 110 >= reactor_percentage >= 90:
        return "NORMAL"
    else:
        return "DANGER"