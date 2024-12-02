def calculateExponent(base, exponent):
    # Step 1: Initialize the result variable to 1
    result = 1
    
    # Step 2: Use a loop to multiply the base by itself exponent times
    for i in range(exponent):  # Loop from 0 to exponent-1
        # Step 3: Multiply the current result by the base
        result = result * base
        # Step 4: Print intermediate result for understanding (optional)
        print(f"After step {i + 1}, result = {result}")
    
    # Step 5: Return the final result
    return result

# Example 1
print("Example 1: 5^5")
print(f"Result: {calculateExponent(5, 5)}")  # ➞ 3125

# Example 2
print("\nExample 2: 10^10")
print(f"Result: {calculateExponent(10, 10)}")  # ➞ 10000000000

# Example 3
print("\nExample 3: 3^3")
print(f"Result: {calculateExponent(3, 3)}")  # ➞ 27
