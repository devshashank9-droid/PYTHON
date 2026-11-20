class Employee:
    company = "Itc"
    name = "default"
    def show(self):
        print(f"THe name of the company is {self.name} and salary is {self.salary}")

# class Programmer:
#     company = "Itc Infotech"
#     def show(self):
#         print(f"THe name of the company is {self.name} and salary is {self.salary}")

#     def showlanguage(self):
#          print(f"THe name is {self.name} and he code in {self.language}")

class programmer(Employee):
    company = "Itc infotech"
    def showlanguage(self):
        print(f"THe name is {self.name} and he code in {self.language}")

a = Employee()
b = programmer()

print(a.company, b.company)