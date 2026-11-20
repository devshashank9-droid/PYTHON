import random
n = random.randint(1, 100)
a = -1

count = 1

while(a != n):
    
    a = int(input("Guess the number : "))
    
        
    if(a < n):
        print("Choose a bigger number")
        count += 1
    elif(a > n):
        print("Choose a smaller number")
        count += 1

print(f"You have guessd {n} perfectly in {count} times")
