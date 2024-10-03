def print_for_loop():
    for i in range(3):
        print(i)

def print_while_loop():
    print("************")
    i = 0    
    while i < 3:
        print(i)
        i += 1

def print_nested_loops():
    for i in range(3):
        print("i:", i)
        for j in range(3):
            print("j:", j)

if __name__ == "__main__":
    print_for_loop()
    print_while_loop()
    print_nested_loops()
