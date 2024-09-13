x = [2,4,8,12]

def getAVG(x):
    z = 0  
    for i in x :
     z =z + i
    N = len(x)
    M = z/N
    return M
    
y = getAVG(x)
for i in x:
        if i > y :
            print(i)
