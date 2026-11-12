
def greatest(a, b, c):
    if(a>b and a>c):
        return a
    elif(b>a and b>c):
        return b
    else:
        return c



a = 3
b = 6
c = 78

print(f"the greatest is : {greatest(a,b,c)}")