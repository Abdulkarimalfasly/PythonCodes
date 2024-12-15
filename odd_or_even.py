# Define a function to check if the length of a string is odd or even
def oddOrEven(s):
    # Calculate the length of the string
    length_of_string = len(s)
    
    # Check if the length is divisible by 2 with no remainder
    if length_of_string % 2 == 0:
        return True  # Return True if the length is even
    else:
        return False  # Return False if the length is odd

# Examples of how to use the function
print(oddOrEven("apples"))  # ➞ True (6 characters, even length)
print(oddOrEven("pears"))   # ➞ False (5 characters, odd length)
print(oddOrEven("cherry"))  # ➞ True (6 characters, even length)
