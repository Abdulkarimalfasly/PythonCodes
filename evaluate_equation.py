# Function to evaluate a mathematical equation given as a string
def equation(eq):
    try:
        # Use eval to compute the result of the equation
        return eval(eq)
    except Exception as e:
        # Handle any errors and return a descriptive message
        return f"Error in evaluating equation: {e}"

# Examples to test the function
print(equation("1+1"))         # ➞ 2
print(equation("7*4-2"))       # ➞ 26
print(equation("1+1+1+1+1"))   # ➞ 5
