"""Functions which helps the locomotive engineer to keep track of the train..."""
def get_list_of_wagons(*args: int) -> list:
    """Return a list of wagons.
 
    :param: arbitrary number of wagons.
    :return: list - list of wagons.
    """
    return list(args)
def fix_list_of_wagons(each_wagons_id: list, missing_wagons: list) -> list:
    """Fix the list of wagons.
 
    :parm each_wagons_id: list - the list of wagons.
    :parm missing_wagons: list - the list of missing wagons.
    :return: list - list of wagons.
    """
    return [each_wagons_id[2]] + missing_wagons + each_wagons_id[3:] + each_wagons_id[:2]
def add_missing_stops(route: dict, **kwargs) ->dict:
    """Add missing stops to route dict.
 
    :param route: dict - the dict of routing information.
    :param: arbitrary number of stops.
    :return: dict - updated route dictionary.
    """
    route['stops'] = list(kwargs.values())
    return route
def extend_route_information(route: dict, more_route_information: dict) -> dict:
    """Extend route information with more_route_information.
 
    :param route: dict - the route information.
    :param more_route_information: dict -  extra route information.
    :return: dict - extended route information.
    """
    return route | more_route_information
def fix_wagon_depot(wagons_rows: list) -> list:
    """Fix the list of rows of wagons.
 
    :param wagons_rows: list[list[tuple]] - the list of rows of wagons.
    :return: list[list[tuple]] - list of rows of wagons.
    """
    return [[row[i] for row in wagons_rows] for i in range(len(wagons_rows))]

