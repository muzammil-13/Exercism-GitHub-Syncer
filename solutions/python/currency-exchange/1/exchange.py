"""Functions for calculating steps in exchaning currency.

Python numbers documentation: https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex

Overview of exchanging currency when travelling: https://www.compareremit.com/money-transfer-tips/guide-to-exchanging-currency-for-overseas-travel/
"""



def exchange_money(budget, exchange_rate):
    """

    :param budget: float - amount of money you are planning to exchange.
    :param exchange_rate: float - unit value of the foreign currency.
    :return: float - exchanged value of the foreign currency you can receive.
    """

    return budget / exchange_rate


def get_change(budget, exchanging_value):
    """

    :param budget: float - amount of money you own.
    :param exchanging_value: float - amount of your money you want to exchange now.
    :return: float - amount left of your starting currency after exchanging.
    """

    return budget - exchanging_value


def get_value_of_bills(denomination, number_of_bills):
    """

    :param denomination: int - the value of a bill.
    :param number_of_bills: int - total number of bills.
    :return: int - calculated value of the bills.
    """

    return denomination * number_of_bills


def get_number_of_bills(amount, denomination):
    """

    :param amount: float - the total starting value.
    :param denomination: int - the value of a single bill.
    :return: int - number of bills that can be obtained from the amount.
    """

    return int(amount//denomination)


def get_leftover_of_bills(amount, denomination):
    """
    Calculate the leftover amount that cannot be exchanged into bills.
    
    :param amount: float - the total starting value.
    :param denomination: int - the value of a single bill.
    :return: float - the leftover amount after exchanging into bills.
    """
    return amount % denomination

# Example usage:
print(get_leftover_of_bills(127.5, 20))  # Output should be 7.5



def exchangeable_value(budget, exchange_rate, spread, denomination):
    """
    Calculate the maximum value of new currency after exchange rate and spread.
    
    :param budget: float - the amount of money you are planning to exchange.
    :param exchange_rate: float - the amount of domestic currency equal to one unit of foreign currency.
    :param spread: int - the percentage taken as an exchange fee.
    :param denomination: int - the value of a single bill of the new currency.
    :return: int - maximum value of the new currency that can be exchanged (as an integer).
    """
    actual_exchange_rate = exchange_rate * (1 + spread / 100)
    exchanged_value = budget / actual_exchange_rate
    return int(exchanged_value // denomination * denomination)

# Example usage:
print(exchangeable_value(127.25, 1.20, 10, 20))  # Output should be 80
print(exchangeable_value(127.25, 1.20, 10, 5))   # Output should be 95

    