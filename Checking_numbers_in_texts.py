x = input("Enter string: ")

numbers = ["1","2","3","4","5","6","7","8","9"]
found = False
for i in x :
    # if i in "123456789":
    if i in numbers:
      found = True
      break
print(found)
