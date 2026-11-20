class Employee:
    
    salary = 5000000    #This is a class attribute
    language = "C++"

shashank = Employee()
shashank.name = "Shashank"       # this is an instance attribute
print(shashank.salary, shashank.language)

rohan = Employee()
rohan.name = "Rohan das"
print(rohan.salary, rohan.language)

# here name is instance attribute and salry and language is class attribute