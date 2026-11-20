class Programmer:
    company = "Microsoft"

    def __init__(self, name, salary, pin):
        self.name = name
        self.salary = salary
        self.pin = pin

p = Programmer("Shashank", 120000, 843114)
print(p.name, p.pin, p.company)

r = Programmer("Rohan", 120000, 843114)
print(r.name, r.pin, r.company)

