
import random

turns = ["rock", "paper", "scissors"]

human_turn = input("Enter rock, scissors or paper: ")
if human_turn != "rock" and human_turn != "scissors" and human_turn != "paper":
    print("must choose correct turn!")
    exit()

computer_turn = random.choice(turns)


print(f"human:{human_turn} vs. Computer: {computer_turn}")
print("-----------------------")




if human_turn ==  computer_turn :
    print("it is a draw!")
elif human_turn == "rock" and computer_turn == "scissors":
    print("human wins!")
elif human_turn == "paper" and computer_turn == "rock":
    print("human wins!")
elif human_turn == "scissors" and computer_turn == "paper":
    print("human wins!")
else:
    print("computer wins!")