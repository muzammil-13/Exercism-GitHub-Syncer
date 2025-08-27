def value_of_card(card):
    """Determine the scoring value of a card.

    :param card: str - given card.
    :return: int - value of a given card.  See below for values.

    1.  'J', 'Q', or 'K' (otherwise known as "face cards") = 10
    2.  'A' (ace card) = 1
    3.  '2' - '10' = numerical value.
    """
    face_cards = ['J', 'Q', 'K']
    if card in face_cards:
        return 10
    elif card == 'A':
        return 1
    else:
        return int(card)

def higher_card(card_one, card_two):
    """Determine which card has a higher value in the hand.

    :param card_one, card_two: str - cards dealt in hand.  See below for values.
    :return: str or tuple - resulting Tuple contains both cards if they are of equal value.

    1.  'J', 'Q', or 'K' (otherwise known as "face cards") = 10
    2.  'A' (ace card) = 1
    3.  '2' - '10' = numerical value.
    """
    # Reusing the value_of_card function to get the values of the cards
    value_one = value_of_card(card_one)
    value_two = value_of_card(card_two)

    if value_one > value_two:
        return card_one
    elif value_two > value_one:
        return card_two
    else:
        return card_one, card_two

def value_of_ace(card_one, card_two):
    # Helper function to get the value of a card
    def value_of_card(card):
        if card in ['J', 'Q', 'K']:
            return 10
        elif card == 'A':
            return 11
        else:
            return int(card)

    # Calculate the current total value of the hand without the ace
    current_total = value_of_card(card_one) + value_of_card(card_two)

    # If adding 11 would go over 21, return 1, otherwise return 11
    if current_total + 11 > 21:
        return 1
    else:
        return 11

# Examples:
print(value_of_ace('6', 'K')) # Output: 1
print(value_of_ace('7', '3')) # Output: 11


def is_blackjack(card_one, card_two):
    """Check if the hand is a blackjack.

    :param card_one, card_two: str - cards dealt.
    :return: bool - True if the hand is a blackjack, False otherwise.

    A blackjack is an ace and a ten-card (10, K, Q, or J).
    """
    # Check if one card is an ace and the other is a ten-card
    return ((card_one == 'A' and card_two in ['10', 'J', 'Q', 'K']) or
            (card_two == 'A' and card_one in ['10', 'J', 'Q', 'K']))

# Examples:
print(is_blackjack('A', 'K'))  # Output: True
print(is_blackjack('10', '9')) # Output: False

def can_split_pairs(card_one, card_two):
    """Determine if a hand can be split into pairs.

    :param card_one, card_two: str - cards dealt.
    :return: bool - True if the hand can be split, False otherwise.

    A hand can be split if both cards have the same value.
    """
    # Check if both cards are face cards or have the same numerical value
    return (card_one in ['J', 'Q', 'K'] and card_two in ['J', 'Q', 'K']) or value_of_card(card_one) == value_of_card(card_two)

# Examples:
print(can_split_pairs('Q', 'K'))  # Output: True
print(can_split_pairs('10', 'A')) # Output: False

def can_double_down(card_one, card_two):
    """Determine if a hand can be doubled down.

    :param card_one, card_two: str - cards dealt.
    :return: bool - True if the hand can be doubled down, False otherwise.

    A hand can be doubled down if the total points are 9, 10, or 11.
    """
    # Calculate the total value of the hand
    total_value = value_of_card(card_one) + value_of_card(card_two)

    # Check if the total value is 9, 10, or 11
    return total_value in [9, 10, 11]

# Examples:
print(can_double_down('A', '9')) # Output: True
print(can_double_down('10', '2')) # Output: False
