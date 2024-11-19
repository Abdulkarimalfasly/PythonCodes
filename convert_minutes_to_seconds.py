# Define a function called "convert" that takes one input parameter: minutes
def convert(minutes):
    # Step 1: Declare a variable to store the result (in seconds)
    seconds = minutes * 60  # Multiply the minutes by 60 to convert to seconds

    # Step 2: Return the result
    return seconds

# Step 3: Test the function with different values
# Example 1: Convert 5 minutes into seconds
result1 = convert(5)  # This will calculate 5 * 60 = 300
print("5 minutes is equal to", result1, "seconds")  # Output: 300 seconds

# Example 2: Convert 3 minutes into seconds
result2 = convert(3)  # This will calculate 3 * 60 = 180
print("3 minutes is equal to", result2, "seconds")  # Output: 180 seconds

# Example 3: Convert 2 minutes into seconds
result3 = convert(2)  # This will calculate 2 * 60 = 120
print("2 minutes is equal to", result3, "seconds")  # Output: 120 seconds
