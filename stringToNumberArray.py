def to_number_array(stringified_numbers):
    # Create an empty list to store the converted numbers
    number_array = []
    
    # Loop through each element in the input array
    for num in stringified_numbers:
        # Convert the string to a floating-point number
        converted_number = float(num)
        
        # Add the converted number to the result list
        number_array.append(converted_number)
    
    # Return the final list of numbers
    return number_array

# Examples
print(to_number_array(["9.4", "4.2"]))  # ➞ [9.4, 4.2]
print(to_number_array(["91", "44"]))    # ➞ [91, 44]
print(to_number_array(["9.5", "8.8"]))  # ➞ [9.5, 8.8]
