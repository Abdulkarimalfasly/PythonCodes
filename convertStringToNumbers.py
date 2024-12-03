def toNumberArray(arr):
    # The function 'toNumberArray' accepts one argument 'arr', which is a list of numbers represented as strings.
    
    # We will use a list comprehension to process each element in the list 'arr'.
    # The list comprehension iterates over every string 'i' in the list 'arr'.
    # For each string, it checks if it contains a decimal point (.) to determine if it should be converted to a float or integer.
    
    # If the string contains a decimal point (.), we use 'float(i)' to convert it to a floating point number.
    # If the string does not contain a decimal point, we use 'int(i)' to convert it to an integer.
    
    return [float(i) if '.' in i else int(i) for i in arr]

# Example usages:
# Calling the function with a list of strings representing integers and floats.
# The result is a list with numbers (either integer or float) instead of strings.
print(toNumberArray(["1", "3", "3.6"]))  # ➞ [1, 3, 3.6]
print(toNumberArray(["9.4", "4.2"]))     # ➞ [9.4, 4.2]
print(toNumberArray(["91", "44"]))       # ➞ [91, 44]
print(toNumberArray(["9.5", "8.8"]))     # ➞ [9.5, 8.8]
