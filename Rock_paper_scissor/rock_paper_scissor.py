import random
while True:
    options=("rock", "paper", "scissor")
    computer=random.choice(options)

    player=input("Enter anyone you want to pick(rock, paper, scissor)").lower()

    if player not in options: 
        print("⚠️Invalid Input! Try Again⚠️")
        continue

    print(f"\nPlayer choose: {player}")
    print(f"Computer Choose: {computer}")

    if player == computer: print("It's a  tie 🟰")
    elif player == "paper" and computer == "rock" or player=="scissor" and computer=="paper" or player =="rock" and computer =="scissor": 
        print("You won 🎉")
    else: print( " You loose 👎")
