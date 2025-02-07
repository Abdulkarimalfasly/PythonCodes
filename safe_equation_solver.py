import re

def equation(expr):
    # Remove any extra spaces
    expr = expr.replace(" ", "")
    
    # Check if the expression contains only numbers and allowed operators (+, -, *, /)
    if not re.fullmatch(r"[0-9+\-*/]+", expr) or "**" in expr:
        return "Invalid equation"
    
    try:
        # Safely evaluate the expression using eval with restricted built-ins
        result = eval(expr, {"__builtins__": None}, {})
        return result
    except Exception as e:
        return f"Error in equation: {e}"

# Test cases
print(equation("1+1"))      # 2
print(equation("7*4-2"))    # 26
print(equation("1+1+1+1+1"))  # 5
print(equation("10/2"))     # 5.0
print(equation("3**2"))     # Invalid equation (now correctly handled)
print(equation("7a+2"))     # Invalid equation
