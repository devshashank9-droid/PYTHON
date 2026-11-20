import random

def game():
    print("You are playing the game..")
    score = random.randint(1,100)
    # Fetch the hiscore
    with open("hiscore.txt") as f:
        hiscore = f.read()
        if(hiscore != ""):
            hiscore = int(hiscore)
        else:
            hiscore = 0

    print(f"Your score : {score}")
    if(score > hiscore):
        with open("hiscore.txt", "w") as f:
            #writ the hiscore to this file
            f.write(str(score))

    return score

game()