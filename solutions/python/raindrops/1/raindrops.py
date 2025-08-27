def convert(number):
    result = ""
    
    if number % 3 == 0:
        result += "Pling"
    if number % 5 == 0:
        result += "Plang"
    if number % 7 == 0:
        result += "Plong"
    
    # If result is stilll an empty string, number was not divisible by 3, 5, or 7
    if result == "":
        result = str(number)
    
    return result