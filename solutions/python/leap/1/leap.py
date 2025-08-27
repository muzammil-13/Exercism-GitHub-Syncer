def leap_year(year):
    """
    Check if a given year is a leap year.,

    :param year: int - the year to check.
    :return: bool - True if the year is a leap year, False otherwise.
    """
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False