def yeah_nope(bool):
    # Check if the value is True or False
    if bool:
        result = "yeah"  # If the value is True
    else:
        result = "nope"  # If the value is False
    
    # Return the result after the check
    return result

# Examples of usage:
print(yeah_nope(True))   # ➞ "yeah"
print(yeah_nope(False))  # ➞ "nope"
