def mult(a, b, c):
    return a*b*c

print(mult(2,3,4))

def rootBeer(x):
    while x>0:
        print(x, "bottles of root beer on the wall")
        x = x - 1 #or x-=1
        
num = int(input("give me a number"))
rootBeer(num) #function call
