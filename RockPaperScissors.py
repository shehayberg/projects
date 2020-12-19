
import random

choices = ["rock", "paper", "scissors"]

user_choice = input("What do you choose? Type rock, paper, or scissors -> ")

computer_choice = random.choice(choices)

print(f"The computer chooses {computer_choice}")

if user_choice == "rock" and computer_choice == "rock":
    print("nobody wins. Play again.")
elif user_choice == "rock" and computer_choice == "paper":
    print("You lose!")
elif user_choice == "rock" and computer_choice == "scissors":
    print("You win!")
elif user_choice == "paper" and computer_choice == "rock":
    print("You lose!")
elif user_choice == "paper" and computer_choice == "paper":
    print("Nobody wins. Play again.")
elif user_choice == "paper" and computer_choice == "scissors":
    print("You lose!")
elif user_choice == "scissors" and computer_choice == "rock":
    print("You lose!")
elif user_choice == "scissors" and computer_choice == "paper":
    print("You win!")
elif user_choice == "scissors" and computer_choice == "scissors":
    print("Nobody wins. Play again.")




