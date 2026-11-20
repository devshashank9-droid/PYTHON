class Employee:
    language = "C++"
    salary = 120000

    def __init__(self, name, salary, language): #dunder method is automatically called
        self.name = name
        self.salary = salary
        self.language = language
        print("This is an constructor")
        
    
    def getInfo(self):
        print(f"The language is {self.language}. The salary is {self.salary}")

    @staticmethod   # by this we donot need self for function does not reciving objects
    def greet():
        print("Good morning")

shashank = Employee("Shashank", 120000, "C++")
shashank.greet()
print(shashank.name, shashank.salary, shashank.language)
