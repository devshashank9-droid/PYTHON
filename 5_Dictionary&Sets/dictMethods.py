marks = {
    "Shashank" : 45,
    "Anish" : 7,
    "Rohit" : 18,
    1 : "Rahul"
}
print(marks)
print(marks.items())
print(marks.keys())  # prints left entities
print(marks.values()) # print right entities
marks.update({"Shashank" : 18, "Anushka" : 99}) # update dictionary (change or add)
print(marks)

print(marks.get("Anushka"))
print(marks.get("Anjali"))  # gives none
print(marks.get["Anjali"])  # gives none with error