marks1 = int(input("Enter Marks 1: "))
marks2 = int(input("Enter Marks 2: "))
marks3 = int(input("Enter Marks 3: "))

totalPercentage = (marks1 + marks2 + marks3)/300 * 100

print("Your percentage is : ", totalPercentage)
if(totalPercentage >= 90 and totalPercentage <= 100):
    print("You topped!!!Congrats")
elif(totalPercentage >= 60 and totalPercentage < 90):
    print("Well done!! You are passed")
elif(totalPercentage >= 30 and totalPercentage < 60):
    print("Improve your marks")
else:
    print("you are failed")