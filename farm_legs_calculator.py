def animals(chickens, cows, pigs):
    # Calculate the number of legs for chickens
    chicken_legs = chickens * 2
    print(f"Chicken legs: {chicken_legs}")  # Debugging step (optional)

    # Calculate the number of legs for cows
    cow_legs = cows * 4
    print(f"Cow legs: {cow_legs}")  # Debugging step (optional)

    # Calculate the number of legs for pigs
    pig_legs = pigs * 4
    print(f"Pig legs: {pig_legs}")  # Debugging step (optional)

    # Sum all the legs to get the total
    total_legs = chicken_legs + cow_legs + pig_legs
    print(f"Total legs: {total_legs}")  # Debugging step (optional)

    # Return the total number of legs
    return total_legs

# Examples
print(animals(2, 3, 5))  # ➞ 36
print(animals(1, 2, 3))  # ➞ 22
print(animals(5, 2, 8))  # ➞ 50
