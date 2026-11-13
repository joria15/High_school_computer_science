"""
author: Anthony Antczak
date: 10/03/2024
Making with iterations
"""
import random
#input
play = input("Do you want to play: ")
play == "yes" # Does play equal yes
play != "no" # Does play not equal no
while play != "no":
        

    computer_choice = None
    random_int = random.randint(1,3)

    if random_int == 1:
        computer_choice = "rock"
    elif random_int == 2:   
        computer_choice = "paper"
    else:
        computer_choice = "scissors"

    move = input("Enter a choice (rock, paper, scissors): ")
    #processing
    #output
    while move != "rock" and move!= "paper" and move!= "scissors":
        input("pick either (rock, paper, scissors)")
# while play == "yes":
    if computer_choice == "rock" and move == "paper":
        print(f"You win! {move} covers {computer_choice}")
        # play = input("Do you want to play: ")
    elif computer_choice == "scissors" and move == "paper":
        print(f"You lose! {computer_choice} cuts {move}")
        # play = input("Do you want to play: ")
    elif computer_choice == "paper" and move == "paper":
        print(f"It's a tie!")
        # play = input("Do you want to play: ")
    elif computer_choice == "rock" and move == "scissors":
        print(f"You lose! {computer_choice} smashes {move}")
        # play = input("Do you want to play: ")
    elif computer_choice == "scissors" and move == "scissors":
        print(f"It's a tie!")
        # play = input("Do you want to play: ")
    elif computer_choice == "paper" and move == "scissors":
        print(f"You win! {move} cuts {computer_choice}")
        # play = input("Do you want to play: ")
    elif computer_choice == "rock" and move == "rock":
        print(f"It's a tie!")
        # play = input("Do you want to play: ")
    elif computer_choice == "scissors" and move == "rock":
        print(f"You win! {move} smashes {computer_choice}")
        # play = input("Do you want to play: ")
    elif computer_choice == "paper" and move == "rock":
        print(f"You lose! {computer_choice} covers {move}")
    
    play = input("Do you want to play: ")