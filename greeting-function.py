# Define the function in a detailed way
def hello_name(name):
    # Step 1: Create a greeting message using string concatenation
    greeting = "Hello " + name + "!"  # Concatenate "Hello", the name, and an exclamation mark
    # Step 2: Return the final greeting message
    return greeting

# Step 3: Call the function with different names and store the results in variables
result1 = hello_name("Gerald")  # Call the function with the name "Gerald"
result2 = hello_name("Tiffany") # Call the function with the name "Tiffany"
result3 = hello_name("Ed")      # Call the function with the name "Ed"

# Step 4: Print the results to the screen
print(result1)  # This will print: Hello Gerald!
print(result2)  # This will print: Hello Tiffany!
print(result3)  # This will print: Hello Ed!

