# Define a function to convert hours into seconds
def howManySeconds(hours):
    # Step 1: Convert hours to minutes
    minutes = hours * 60  # Each hour has 60 minutes
    print(f"{hours} hours contain {minutes} minutes.")  # Print the result

    # Step 2: Convert minutes to seconds
    seconds = minutes * 60  # Each minute has 60 seconds
    print(f"{minutes} minutes contain {seconds} seconds.")  # Print the result

    # Step 3: Return the final result
    return seconds  # Return the total number of seconds

# Examples of using the function
result1 = howManySeconds(2)   # Example 1: Two hours
print(f"Final result: {result1} seconds.\n")

result2 = howManySeconds(10)  # Example 2: Ten hours
print(f"Final result: {result2} seconds.\n")

result3 = howManySeconds(24)  # Example 3: Twenty-four hours
print(f"Final result: {result3} seconds.\n")
