def futurePeople(population, n):
    # Calculate the number of decades
    decades = 3
    years = decades * 10  # Each decade has 10 years

    # Calculate the total number of months in 30 years
    months_per_year = 12  # Each year has 12 months
    total_months = years * months_per_year

    # Calculate the total number of new people born during this period
    total_new_people = n * total_months

    # Add the total number of new people to the current population
    future_population = population + total_new_people

    # Return the future population
    return future_population

# Example usage
print(futurePeople(256, 2))  # ➞ 976
print(futurePeople(3248, 6))  # ➞ 5408
print(futurePeople(5240, 3))  # ➞ 6320
