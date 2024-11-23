def repeat_start(word):
    # Extract the first two letters of the word
    first_two = word[:2]
    
    # Construct the sentence with repetition and ellipsis
    return f"{first_two}... {first_two}... {word}?"

# Examples to test the code
print(repeat_start("incredible"))  # Output: "in... in... incredible?"
print(repeat_start("enthusiastic"))  # Output: "en... en... enthusiastic?"
print(repeat_start("outstanding"))  # Output: "ou... ou... outstanding?"
