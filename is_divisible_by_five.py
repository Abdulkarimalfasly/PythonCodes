def divisibleByFive(num):
    # Check if the number is evenly divisible by 5
    if num % 5 == 0:
        return True  # Return True if divisible
    else:
        return False  # Return False if not divisible

# Test cases
print(divisibleByFive(5))    # True
print(divisibleByFive(-55))  # True
print(divisibleByFive(37))   # False
