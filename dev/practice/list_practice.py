"""
author: Anthony Antczak
date: 10/16/2024
Practicing with lists
"""
# Input
names = []
user_input = str(input("Enter a name (or a blank to stop): "))
names.append(user_input)
johndoe = 0
# Processing
while not user_input == "":
    if user_input == "John":
        johndoe = (johndoe+1)
    user_input = str(input("Enter a name or a blank to stop: "))
    if user_input != "":
        names.append(user_input)

percentage = johndoe/len(names)*100   

# Output
print(f"{percentage}% of the names are john")