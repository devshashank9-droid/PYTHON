name  = "Shashank"

print(name)


shortName = name[3:7] # start from the index 1 and go to index 3(excluding 3)
print(shortName)
print(name[3:8])  # shortcut

print(name[:4]) # is same as [0:4]
print(name[3:]) # is same as [3:8]

print(name[-4:-1])   # negative slicing
print(name[1:4])

print(name[0:8:2]) # skipping some chars