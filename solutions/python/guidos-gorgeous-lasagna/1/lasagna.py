
EXPECTED_BAKE_TIME = 40

def bake_time_remaining(remain_time):
    """Calculating:
    Remaining bake time"""
    return EXPECTED_BAKE_TIME - remain_time
    
def preparation_time_in_minutes(number_of_layers):
    """Calculating:
    Preparation time"""
    return number_of_layers * 2

    
def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    """Calculate:
    The elapsed cooking time.
    """
    return number_of_layers * 2 + elapsed_bake_time