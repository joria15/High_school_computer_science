"""
author: Anthony Antczak
date: 11/07/2024
File input practicing!
"""
#processing
def spookify_word(word: str) -> str:  # Don't forget type annotations (I gave them to you lol)
    """Takes a string and makes it scarier
    >>> spookify("Fear")
    fEAR
    >>> spookify("Hello")
    hELLO
    """
    # xs = word
    # s = " ".join(str(x) for x in xs)

    # words = sentence.split()
    # new_words = []
    # for word in words:
    f = word[0]
    u = word[1:].upper()
    l = f.lower()
    c = l + u
    return c
    #     new_words.append(c)
    # return " ".join(new_words)


def spookify_sentence(sentence): # Don't forget type annotations (I gave them to you lol)
    """"""
    words = sentence.split()  # This is a list of strings
    transformed_words = []
    for word in words:
        # Transform each word here
        transformed_words.append(spookify_word(word))

    return " ".join(transformed_words)




def main():
    #input
    story = [
    "It was a dark and stormy night, and a cold wind howled through the trees.",
    "In the shadows of the old, abandoned mansion, a faint light flickered from an upper window.",
    "A brave but frightened adventurer named Alex crept closer, clutching a rusty flashlight.",
    "As Alex stepped onto the porch, the floorboards groaned underfoot, echoing through the empty halls.",
    "Suddenly, the flashlight flickered, casting eerie shadows that seemed to move on their own.",
    "In the dim light, Alex spotted an ancient, dusty book lying open on the floor.",
    "The words seemed to glow as if whispering secrets from beyond the grave.",
    "Just then, a cold hand reached out from the shadows, and Alex felt a chill run down their spine...",
    "Frozen in fear, Alex turned around slowly, heart pounding, but no one was there.",
    "And then, from the darkness, a whisper: 'You should not have come here...'"
    ]

    spooky_story = []

    # Do the list transformation
    #processing
    for sentence in story:
        spooky_story.append(spookify_sentence(sentence))
        #output
    print('\n'.join(spooky_story))


if __name__ == "__main__":
    main()