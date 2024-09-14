def getAVG(x):
    z = 0  
    for i in x:
        z += i
    N = len(x)
    M = z / N
    return M

x = [12,43,56,78,67,45,34,23,45,67,89]  
y = getAVG(x)

for i in x:
    if i > y:
        print(i)
