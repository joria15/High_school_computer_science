"""
author: Anthony Antczak
date: 09/19/2024
A conditional investigation
"""

# Input
is_cold_outside = False
favourite_number = 15
name_of_hero = "Batman"
e = 2.5777
birthday_number = 9

# Processing

# Output

if is_cold_outside:
    print("Geez man, I'm freezing")
else:
    print("I'm glad I didn't bring a jacket")


if favourite_number < 10:
    print("You have pretty low standards 👀")
elif favourite_number < 20:
    print("You've got an alright personality ⭐")
elif favourite_number < 30:
    print("There are some good people in this world 🤗")
elif favourite_number < 40:
    print("Faith in humanity restored 🎉")
else:
    print("You must control life, the universe, and everything 🤯")


if "e" in name_of_hero:
    print("You probably have a pretty mid hero")
elif "x" in name_of_hero:
    print("Your hero is pretty cool")

if name_of_hero.lower() == "the flash":
    print("Dawg, your zoomin!")
elif name_of_hero.lower() == "superman":
    print("🙄")
else:
    print("Is it even a superhero??")

if e > 3:
    print("Incorrect")
elif e < 2:
    print("Also incorrect")
else:
    print("You probably got it!")

# Check to see if a number is a float
if int(e) == e:
    print("e must be a whole number")
else:
    print("e must have decimals")

if birthday_number >= 15:
    print("special person you are")
else:
    print("always on the low end of number huh?")