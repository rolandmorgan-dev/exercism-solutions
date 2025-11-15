"""Functions which helps the locomotive engineer to keep track of the train."""

def get_list_of_wagons(*args):
    """Return a list of wagons.

    :param: arbitrary number of wagons.
    :return: list - list of wagons.
    """
    return list(args)

def fix_list_of_wagons(each_wagons_id, missing_wagons):
    """Fix the list of wagons.

    :param each_wagons_id: list - the list of wagons.
    :param missing_wagons: list - the list of missing wagons.
    :return: list - list of wagons.
    """
    [a, b, c, *rest_wagons] = each_wagons_id
    *fixed_wagons, = *[c], *missing_wagons, *rest_wagons + [a, b]
    return fixed_wagons

def add_missing_stops(*args,**kwargs):
    """Add missing stops to route dict.

    :param route: dict - the dict of routing information.
    :param: arbitrary number of stops.
    :return: dict - updated route dictionary.
    """
    stops, destination = list(kwargs.values()), args[0]
    destination['stops'] = stops
    return destination

def extend_route_information(route, more_route_information):
    """Extend route information with more_route_information.

    :param route: dict - the route information.
    :param more_route_information: dict -  extra route information.
    :return: dict - extended route information.
    """
    *extended, = *route.items(), *more_route_information.items()
    return dict(extended)

def fix_wagon_depot(wagons_rows):
    """Fix the list of rows of wagons.

    :param wagons_rows: list[list[tuple]] - the list of rows of wagons.
    :return: list[list[tuple]] - list of rows of wagons.
    """
    *fixed_order, = zip(*wagons_rows)
    fixed_wagons = []
    for line in fixed_order:
        fixed_wagons.append(list(line))
    return fixed_wagons