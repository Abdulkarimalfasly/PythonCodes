def returnNegative(number):
    # Check if the number is less than or equal to zero
    if number <= 0:
        # If the number is negative or zero, return it as is
        return number
    else:
        # If the number is positive, return it with a negative sign
        return -number

# Examples of usage:
print(returnNegative(4))   # ➞ -4
print(returnNegative(15))  # ➞ -15
print(returnNegative(-4))  # ➞ -4
print(returnNegative(0))   # ➞ 0
