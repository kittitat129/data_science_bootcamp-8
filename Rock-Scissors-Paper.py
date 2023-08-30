# import sample from random
from random import sample

# list of paoyingchub choice
choice = ["rock", "scissor", "paper"]

def pao_ying_chub():
    score_you = 0
    score_bot = 0
    while True:
        bot = sample(choice, 1)[0]
        rsp = input("Rock Scissor or Paper?")
        if rsp == bot:
            print("Tie")
        elif rsp.lower() == "rock":
            if bot == "scissor":
                score_you += 1
                print(f"You win. You score: {score_you}, Bot score {score_bot}")
            else:
                score_bot += 1
                print(f"You lose. You score: {score_you}, Bot score {score_bot}")
        elif rsp.lower() == "scissor":
            if bot == "paper":
                score_you += 1
                print(f"You win. You score: {score_you}, Bot score {score_bot}")
            else:
                score_bot += 1
                print(f"You lose. You score: {score_you}, Bot score {score_bot}")
        elif rsp.lower() == "paper":
            if bot == "rock":
                score_you += 1
                print(f"You win. You score: {score_you}, Bot score {score_bot}")
            else:
                score_bot += 1
                print(f"You lose. You score: {score_you}, Bot score {score_bot}")
        elif rsp.lower() == "quit":
            return("See you again :)")
        else:
            print("Invalid answer, please try again!")
