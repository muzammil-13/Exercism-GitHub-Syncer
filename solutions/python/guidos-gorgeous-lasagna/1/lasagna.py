EXPECTED_BAKE_TIME = 40  # Expected bake time in minutes

def bake_time_remaining(elapsed_bake_time):
    """Calculate the bake time remaining.

    This function takes the actual minutes the lasagna has been in the oven as
    an argument and returns how many minutes the lasagna still needs to bake
    based on the `EXPECTED_BAKE_TIME`.

    :param elapsed_bake_time: int - baking time already elapsed.
    :return: int - remaining bake time (in minutes) derived from 'EXPECTED_BAKE_TIME'.
    """
    return EXPECTED_BAKE_TIME - elapsed_bake_time

PREPARATION_TIME = 2  # Preparation time per layer in minutes

def preparation_time_in_minutes(number_of_layers):
    """Calculate the preparation time.

    This function takes the number of layers as an argument and returns
    the total preparation time based on a predefined `PREPARATION_TIME` per layer.

    :param number_of_layers: int - number of lasagna layers.
    :return: int - total preparation time in minutes.
    """
    return PREPARATION_TIME * number_of_layers

def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    """Calculate the total elapsed cooking time.

    This function takes two integers representing the number of lasagna layers and the
    time already spent baking and calculates the total elapsed minutes spent cooking the
    lasagna, including both preparation and baking times.

    :param number_of_layers: int - the number of layers in the lasagna.
    :param elapsed_bake_time: int - elapsed cooking time.
    :return: int - total time elapsed (in minutes) preparing and cooking.
    """
    return preparation_time_in_minutes(number_of_layers) + elapsed_bake_time
