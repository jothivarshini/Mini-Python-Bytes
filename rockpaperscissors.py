                                                                                        ### Rock Paper Scissors Program ###
#import choices and take the inputs
import random
user_choice = input("Enter choice (rock, paper, scissors): ")
computer_choice = ["rock", "paper", "scissors"]

#allow the computer to make a random choice and print user and computer choices
computer_choice = random.choice(choices)
print(f"\n You chose {user_choice}, computer chose {computer_choice}.\n")

#if-elif-else block case to determine a winner
if user_choice == computer_choice:
    print(f"Both players selected {user_choice}. It's a tie!")
elif user_choice == "rock":
    if computer_choice == "scissors"
        print("Rock beats scissors! You win!")
    else:
        print("Paper covers rock! Computer wins")
elif user_choice == "paper":
    if computer_choice == "rock"
        print("Paper covers rock! You win!")
    else:
        print("Scissors cuts paper! Computer wins")
elif user_choice == "scissors":
    if computer_choice =="paper":
        print("Scissors cuts paper! You win!")
    else:
        print("Rock beats scissors! Computer wins")

    

