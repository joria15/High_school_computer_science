"""
author: Anthony Antczak
date: 11/06/2024
Making with functions
"""
#input
def main():
    adjective_entered = str(input("enter an adjective: "))
    noun_entered = str(input("enter an noun: "))
    verb_entered = str(input("enter an verb: "))
    noun_entered2 = str(input("enter an noun: "))
    #processing
    with open ("game.txt", mode="r") as f_in:
        story = f_in.read()
        story = story.replace("ADJECTIVE", adjective_entered, 1)
        story = story.replace("NOUN", noun_entered, 1)
        story = story.replace("VERB", verb_entered, 1)
        story = story.replace("NOUN", noun_entered2, 2)
         #output
        print(story)

if __name__ == "__main__":
    main()