class Employee:
    language = "C++"
    salary = 120000

    def getInfo(self):
        print(f"The language is {self.language}. The salary is {self.salary}")
    def greet(self):
        print("Good morning")

shashank = Employee()
shashank.greet()
shashank.getInfo()
