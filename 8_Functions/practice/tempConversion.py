def FtoC(f):
    return 5*(f-32)/9

f = int(input("Enter temperature in F: "))
c = FtoC(f)
print(f"{round(c, 2)} C")