numbers = (23,345,567,23,45,67,89,56,3456,5768,3445,7876,6534)

def largest_num(numbers):
    largest = 0
    for i in numbers:
        if i > largest:
            largest = i
    return largest

largest = largest_num(numbers)
print("The largest number is:", largest)
