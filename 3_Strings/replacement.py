letter = '''Dear <|Name|>,
You are selected !
<|Date|> '''

print(letter.replace("<|Name|>", "Shashank").replace("<|Date|>", "13 Aug 2029"))