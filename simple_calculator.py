def operate(num1, num2, operator):
    # Check if the operator is addition
    if operator == "+":
        # Perform addition and return the result
        return num1 + num2
    # Check if the operator is subtraction
    elif operator == "-":
        # Perform subtraction and return the result
        return num1 - num2
    # Check if the operator is multiplication
    elif operator == "*":
        # Perform multiplication and return the result
        return num1 * num2
    # Check if the operator is division
    elif operator == "/":
        # Perform division and return the result
        return num1 / num2
    # Check if the operator is modulus (remainder of division)
    elif operator == "%":
        # Perform modulus operation and return the result
        return num1 % num2
    # If the operator is not recognized
    else:
        # Return a message for invalid operator
        return "Invalid operator"

# Test cases
print(operate(1, 2, "+"))  # Output: 3 (1 + 2)
print(operate(7, 10, "-"))  # Output: -3 (7 - 10)
print(operate(20, 10, "%")) # Output: 0 (20 % 10)
