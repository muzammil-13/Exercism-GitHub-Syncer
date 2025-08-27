"""Functions for implementing the rules of the classic arcade game Pac-Man."""


def eat_ghost(power_pellet_active, touching_ghost):
    """Verify that Pac-Man can eat a ghost if he is empowered by a power pellet.

    :param power_pellet_active: bool - does the player have an active power pellet?
    :param touching_ghost: bool - is the player touching a ghost?
    :return: bool - can a ghost be eaten?
    """

    return power_pellet_active and touching_ghost


def score(touching_power_pellet, touching_dot):
    """Verify that Pac-Man has scored when a power pellet or dot has been eaten.

    :param touching_power_pellet: bool - is the player touching a power pellet?
    :param touching_dot: bool - is the player touching a dot?
    :return: bool - has the player scored or not?
    """
    return touching_power_pellet or touching_dot


# The lose function from part 3 for reference
def lose(power_pellet_active, touching_ghost):
    """Determine if Pac-Man loses.

    :param power_pellet_active: bool - is a power pellet active?
    :param touching_ghost: bool - is Pac-Man touching a ghost?
    :return: bool - True if Pac-Man loses, False otherwise.
    """
    return not power_pellet_active and touching_ghost


def win(has_eaten_all_dots, power_pellet_active, touching_ghost):
    """Determine if Pac-Man wins.

    :param has_eaten_all_dots: bool - has Pac-Man eaten all of the dots?
    :param power_pellet_active: bool - is a power pellet active?
    :param touching_ghost: bool - is Pac-Man touching a ghost?
    :return: bool - True if Pac-Man wins, False otherwise.
    """
    # Pac-Man wins if he has eaten all dots and has not lost (not touching a ghost without a power pellet)
    return has_eaten_all_dots and not lose(power_pellet_active, touching_ghost)