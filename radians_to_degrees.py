# Step 1: Import the math library to use the value of pi
import math

# Step 2: Define the function to convert radians to degrees
def radiansToDegrees(radians):
    """
    This function converts an angle from radians to degrees.
    
    Parameters:
    radians (float): The angle in radians to be converted to degrees.
    
    Returns:
    float: The angle in degrees.
    """
    # Step 3: Calculate degrees using the formula
    degrees = radians * (180 / math.pi)
    
    # Step 4: Return the calculated value
    return degrees

# Step 5: Test the function with example values
# Example 1: Convert 1 radian to degrees
result1 = radiansToDegrees(1)
print(f"1 radian is equal to {result1} degrees.")  # Expected output: 57.29577951308232

# Example 2: Convert 20 radians to degrees
result2 = radiansToDegrees(20)
print(f"20 radians is equal to {result2} degrees.")  # Expected output: 1145.9155902616465

# Example 3: Convert 50 radians to degrees
result3 = radiansToDegrees(50)
print(f"50 radians is equal to {result3} degrees.")  # Expected output: 2864.7889756541163
