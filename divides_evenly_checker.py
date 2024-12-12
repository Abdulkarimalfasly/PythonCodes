def divides_evenly(a, b):
    # Check if a is evenly divisible by b
    if a % b == 0:
        # Print a message if divisible
        print(f"The number {a} is evenly divisible by {b}.")
        return True
    else:
        # Print a message if not divisible
        print(f"The number {a} is not evenly divisible by {b}.")
        return False

# Examples
result1 = divides_evenly(98, 7)
print(f"Result: {result1}")  # True

result2 = divides_evenly(85, 4)
print(f"Result: {result2}")  # False
