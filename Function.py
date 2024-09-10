def checkage(x):
    if x <= 10:
        print("You are a minor")
    elif 10 < x < 20:
        print("You are a young adult")
    elif 20 <= x < 30:
        print("You are an adult")
    elif 30 <= x < 50:
        print("You are a senior")
    else:
        print("You are an elder") 

x = 30
checkage(x)
