def is_leap_year(year):
    """
    Function to check if a given year is a leap year.

    Parameters:
        year (int): The year to be checked.

    Returns:
        bool: True if the year is a leap year, False otherwise.
    """
    # Check if the year is divisible by 4
    if year % 4 == 0:
        # Check if the year is divisible by 100
        if year % 100 == 0:
            # Check if the year is divisible by 400
            if year % 400 == 0:
                return True  # Leap year
            else:
                return False  # Not a leap year
        else:
            return True  # Leap year
    else:
        return False  # Not a leap year


# Example usage
if __name__ == "__main__":
    years = [1990, 1924, 2021, 2000, 1900]
    for year in years:
        print(f"{year} is a leap year: {is_leap_year(year)}")
