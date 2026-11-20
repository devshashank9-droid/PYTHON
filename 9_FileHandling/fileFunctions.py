f = open("file.txt")

line1 = f.readlines()

print(line1, type(line1))

line2 = f.readlines()
print(line2, type(line2))

f.close()