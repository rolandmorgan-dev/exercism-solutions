"""
Reactor control and safety monitoring system.

This module contains functions to check the criticality balance of a reactor,
calculate reactor efficiency based on voltage and current, and monitor the 
safety levels of the reactor based on temperature and neutron emission.

Functions:
- is_criticality_balanced: Determines if the reactor is in a balanced state based 
  on temperature and neutron emission.
- reactor_efficiency: Calculates the reactor's efficiency based on voltage, current, 
  and theoretical max power, and returns a color indicating performance.
- fail_safe: Evaluates the reactor's safety based on temperature and neutrons produced 
  per second, returning a safety status ("LOW", "NORMAL", or "DANGER").
"""
# Reactor Control
def is_criticality_balanced(temperature, neutrons_emitted):
    # Checking reactor balance in criticality
    return temperature < 800 and neutrons_emitted > 500 and (temperature * neutrons_emitted) < 500000
        
def reactor_efficiency(voltage, current, theoretical_max_power):
    # Determining the power output range
    percentage_value = (voltage*current/theoretical_max_power)*100
    if percentage_value >= 80:
        return "green"
    if 60 <= percentage_value < 80:
        return "orange"
    if 30 <= percentage_value < 60:
        return "red"
    return "black"
    
def fail_safe(temperature, neutrons_produced_per_second, threshold):
    # Fail Safe Mechanism
    reactor_percentage = temperature * neutrons_produced_per_second/threshold*100
    if reactor_percentage < 90:
        return "LOW"
    if 110 >= reactor_percentage >= 90:
        return "NORMAL"
    return "DANGER"