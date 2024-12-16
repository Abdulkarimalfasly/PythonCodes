import math  # Importing the math library to get the value of pi (π)

# Define the function to convert radians to degrees
def radiansToDegrees(radians):
    # Calculate the degrees using the formula:
    # degrees = radians * (180 / π)
    degrees = radians * (180 / math.pi)
    
    # Return the calculated degree value
    return degrees

# Test the function with some examples

# Example 1: Convert 1 radian to degrees
radian_value = 1
degree_value = radiansToDegrees(radian_value)
print(f"{radian_value} radian is equal to {degree_value} degrees")

# Example 2: Convert 20 radians to degrees
radian_value = 20
degree_value = radiansToDegrees(radian_value)
print(f"{radian_value} radians is equal to {degree_value} degrees")

# Example 3: Convert 50 radians to degrees
radian_value = 50
degree_value = radiansToDegrees(radian_value)
print(f"{radian_value} radians is equal to {degree_value} degrees")

