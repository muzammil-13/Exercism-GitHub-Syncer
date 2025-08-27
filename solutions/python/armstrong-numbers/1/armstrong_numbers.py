def is_armstrong_number(number):
    # Convert the number to a string to iterate over each digit
    num_str = str(number)
    
    # Calculate the number of digits
    num_digits = len(num_str)
    
    # Initialize sum of powers of digitss
    sum_of_powers = 0
    
    # Calculate sum of each digit raised to the power of num_digits
    for digit_char in num_str:
        digit = int(digit_char)  # Convert character to integer
        sum_of_powers += digit ** num_digits
    
    # Check if the sum of powers is equal to the original number
    return sum_of_powers == number