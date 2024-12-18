def intToString(num):
    # Convert the integer to a string using string formatting
    return f"{num}"

def stringToInt(string):
    # Convert the string to an integer manually
    result = 0
    for char in string:
        result = result * 10 + (ord(char) - ord('0'))
    return result

# Testing the functions and printing results
# Convert an integer to a string
result1 = intToString(4)
print(f"intToString(4) ➞ \"{result1}\"")  # ➞ "4"

# Convert a string to an integer
result2 = stringToInt("4")
print(f"stringToInt(\"4\") ➞ {result2}")  # ➞ 4

# Additional test: Convert a larger integer to a string
result3 = intToString(29348)
print(f"intToString(29348) ➞ \"{result3}\"")  # ➞ "29348"

# Additional test: Convert a larger string to an integer
result4 = stringToInt("29348")
print(f"stringToInt(\"29348\") ➞ {result4}")  # ➞ 29348
