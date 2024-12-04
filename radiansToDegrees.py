import math

def radiansToDegrees(radians):
    # The math module provides the value of pi (π).
    # To convert radians to degrees, we use the formula:
    # Degrees = Radians * (180 / π)
    
    return radians * (180 / math.pi)  # Multiply the radian value by (180 / π)

# Example usages:

# Example 1: Convert 1 radian to degrees
# Expected result: 57.29577951308232
print(radiansToDegrees(1))

# Example 2: Convert 20 radians to degrees
# Expected result: 1145.9155902616465
print(radiansToDegrees(20))

# Example 3: Convert 50 radians to degrees
# Expected result: 2864.7889756541163
print(radiansToDegrees(50))

