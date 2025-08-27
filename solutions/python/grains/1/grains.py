"""Calculate the number of grains of wheat on a chessboard given that the number on each square doubles."""

def square(number):
    if number not in range(1,65):
        raise ValueError("square must be between 1 and 64")
    return 2**(number-1)


def total():
    return 2**64 -1