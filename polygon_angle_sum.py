def sum_polygon(n):
    # Check if the value of n is less than or equal to 2
    if n <= 2:
        # If n is less than or equal to 2, it is not a valid polygon
        return 0
    
    # Use the formula to calculate the sum of interior angles: (n - 2) * 180
    total_internal_angles = (n - 2) * 180
    
    # Return the calculated result
    return total_internal_angles
