#Reactor Control
def is_criticality_balanced(temperature, neutrons_emitted):
    return temperature < 800 and neutrons_emitted > 500 and (temperature * neutrons_emitted) < 500000
        
def reactor_efficiency(voltage, current, theoretical_max_power):
    percentage_value = (voltage*current/theoretical_max_power)*100
    if percentage_value >= 80:
        return "green"
    if 60 <= percentage_value < 80:
        return "orange"
    if 30 <= percentage_value < 60:
        return "red"
    return "black"
    
def fail_safe(temperature, neutrons_produced_per_second, threshold):
    reactor_percentage = temperature * neutrons_produced_per_second/threshold*100
    if reactor_percentage < 90:
        return "LOW"
    if 110 >= reactor_percentage >= 90:
        return "NORMAL"
    return "DANGER"