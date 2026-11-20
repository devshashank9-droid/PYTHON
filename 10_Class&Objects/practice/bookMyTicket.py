from random import randint
class Train:

    def __init__(self, trainno):
        self.trainno = trainno

    def book(self, fro, to):
        print(f"The seat is booked in train no: {self.trainno} from {fro} to {to}")

    def status(self):
        print(f"Train no: {self.trainno} is running on time")

        
    def fare(self, fro, to):
        print(f"Ticket fare in train no : {self.trainno} from {fro} to {to} is {randint(300, 5000)}")

t = Train(12345)
t.book("Delhi", "Ahmedabad")
t.status()
t.fare("Delhi", "Ahmedabad")