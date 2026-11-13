"""
author: Anthony Antczak
date: 11/11/2024
Play a game and collect points
"""
import random


def play_game():
    """Play an intense game, and return the score for that round

    Returns:
        int: The score for playing this round
    """
    return random.randint(1, 50)

# TODO: See instructions on Pycs
def main():
    # Input
    yes_no = input("Do you want to play a game? ")


    # Processing
    scores = []
    # Check to see if the input (when converted to lowercase) 
    # starts with "y"
    while yes_no.lower().startswith("y"):
        # Play the game and print the score
        username = input("Enter your username: ")
        score = play_game()
        print(f"Woah! Nice round. Your score was {score}")

        # Add the score to the scores list. Notice two things
        ## 1. I need to convert score to a str 
        ##    (f_out.writelines() needs a list of strings)
        ## 2. I need to add on a "\n" (new line character) to the end.
        ##    (Take it out and see what happens)
        scores.append(username+": "+str(score)+"\n")

        # Ask again to ensure we don't have an infinite loop
        yes_no = input("Do you want to play a game? ")

    # Output
    # Write all of the scores to a text file scores.txt. 
    # It does not have to exist before we run this program.
    with open("scores.txt", mode="w") as f_out:
        f_out.writelines(scores)


if __name__ == "__main__":
    main()