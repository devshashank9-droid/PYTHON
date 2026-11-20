f = open("poem.txt")
content = f.read()
if("twinkle" in content):
    print("Present")

else:
    print("absent")

f.close()