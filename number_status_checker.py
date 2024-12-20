def evaluate_number(num):
    print("Checking the number...")
    if num == 0:
        print("The number is zero.")
        return True
    else:
        if num > 0:
            print("The number is positive.")
            return "positive"
        else:
            print("The number is negative.")
            return "negative"

# Starting the program
print("This program evaluates if a number is zero, positive, or negative.")
print("Please follow the instructions below.")
number = int(input("Enter a number: "))  # Ask the user for a number
print("Processing your input...")

# Call the function and get the result
result = evaluate_number(number)

print("Evaluation complete!")
print("Final Result:", result)
