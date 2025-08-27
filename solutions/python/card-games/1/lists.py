def get_rounds(number):
    return [number, number + 1, number + 2]

def concatenate_rounds(rounds_1, rounds_2):
    return rounds_1 + rounds_2

def list_contains_round(rounds, number):
    return number in rounds

def card_average(hand):
    return sum(hand) / len(hand)

def approx_average_is_average(hand):
    return (hand[0] + hand[-1]) / 2 == card_average(hand) or hand[len(hand)//2] == card_average(hand)

def average_even_is_average_odd(hand):
    even_cards = hand[0::2]
    odd_cards = hand[1::2]
    return sum(even_cards) / len(even_cards) == sum(odd_cards) / len(odd_cards)

def maybe_double_last(hand):
    if hand[-1] == 11:  # Assuming Jack is represented by 11
        hand[-1] *= 2
    return hand
