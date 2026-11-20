a = int(input("Enter the number: "))
b = int(input("Enter the number: "))

if(b == 0):
    raise ZeroDivisionError("Hey our program is not meant to divide by zero")
else:
    print(f"The division a/b is {a/b}")