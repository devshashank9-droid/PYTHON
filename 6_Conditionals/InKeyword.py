p1 = "Buy now"
p2 = "Win Iphone"
p3 = "You won lot of money"
p4 = "click on the link"

message = input("Enter your message : ")

if((p1 in message) or (p2 in message) or (p3 in message) or (p4 in message)):
    print("This comment is spam")
else:
    print("This comment is not spam")