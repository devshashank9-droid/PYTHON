words = ["fucking", "idiot", "bitch", "bastard"]

with open("censoredWords.txt" , "r") as f:
    content = f.read()

for word in words:
    content = content.replace(word, "*" * len(word))

with open("censoredWords.txt", 'w') as f:
    f.write(content)