import random

choices = ["rock", "paper", "scrissor"]

while true:
    print(":) :) :) Rock Paper Scissor Game----")
    print("choices: ", choice)
    user_choice = input("Enter a Choice(write quit to exit)").lower()

    if user_choice == "quit" :
        print("Game Over")
        break 
    if user_choice not in choices:
        print("invalid choice, write another!")

    computer_choice == random.choice(choices)

    if user_choice == computer_choice:
        print(f"User Choice {user_choice} vs. computer choice
              {computer_choice} = DRAW")
    elif(
        user_choice == "rock" and computer_choice == "scissor"
        or user_choice == "scissor" 