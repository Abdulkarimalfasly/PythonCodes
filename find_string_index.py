# Function to find the index of a string in a list
def find_index(arr, string):
    # Step 1: Check if the list is empty
    if len(arr) == 0:
        print("The list is empty.")
        return -1  # Return -1 if the list is empty

    # Step 2: Loop through the list to find the string
    for i in range(len(arr)):
        print(f"Checking index {i}: {arr[i]}")  # Log each element being checked
        # Step 3: Check if the current element matches the string
        if arr[i] == string:
            print(f"Found '{string}' at index {i}.")  # Log when the string is found
            return i  # Return the index if a match is found

    # Step 4: If no match is found after looping through the entire list
    print(f"'{string}' was not found in the list.")
    return -1  # Return -1 if the string is not found

# Example usage
test_list1 = ["hi", "edabit", "fgh", "abc"]
test_string1 = "fgh"
print(f"Index of '{test_string1}': {find_index(test_list1, test_string1)}")  # ➞ 2

test_list2 = ["Red", "blue", "Blue", "Green"]
test_string2 = "blue"
print(f"Index of '{test_string2}': {find_index(test_list2, test_string2)}")  # ➞ 1

test_list3 = ["a", "g", "y", "d"]
test_string3 = "d"
print(f"Index of '{test_string3}': {find_index(test_list3, test_string3)}")  # ➞ 3

test_list4 = ["Pineapple", "Orange", "Grape", "Apple"]
test_string4 = "Pineapple"
print(f"Index of '{test_string4}': {find_index(test_list4, test_string4)}")  # ➞ 0

# Additional example: Testing with an empty list
empty_list = []
test_string5 = "apple"
print(f"Index of '{test_string5}': {find_index(empty_list, test_string5)}")  # ➞ -1
