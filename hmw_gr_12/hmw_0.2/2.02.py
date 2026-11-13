def position():
    while True:
        acount = 0
        bcount = 0

        word = input("Enter a text of 10 characters or less: ")

        for i in range(len(word)):
            if word[i].lower() == "a":
                acount += 1
            if word[i].lower() == "b":
                bcount += 1
        
        if not word.isalpha():
            print("only letters")
            continue

        if (acount + bcount) < len(word) and len(word) > 10:
            print("only A and B characters and shorter word")
            continue

        if (acount + bcount) < len(word):
            print("only A and B characters")
            continue

        if len(word) > 10:
            print("word has to be less than 10 characters!")
            continue

        if acount % 2 == 0:
            word = word.lstrip("a, A")
            print(word.ljust(20))
            print(word.rjust(20))
            print(word.center(20))
            continue

        else:
            word = word.lstrip("a, A")
            word = word.rstrip("a, A")
            print(word.ljust(20))
            print(word.rjust(20))
            print(word.center(20))
#position()

def num_word():
    numeric_c = 0
    word_c = 0

    word_num = input("Enter a sentence: ")
    word_num = word_num.split()
    print(word_num)

    for word in word_num:
        if word.isnumeric():
            numeric_c += 1
        if word.isalpha():
            word_c += 1
        
    print(f"numneric words: {numeric_c}, only letter words: {word_c}")

# num_word()

def isPalindrome(word):
    cut = (len(word))//2
    cut_odd = cut + 1
    
    if len(word) % 2 != 0:
        if word[:cut] == word[cut_odd:][::-1]:
            return "Palindrome"
        else:
            return "nope"
            

    if word[:cut] == word[cut:][::-1]:
        return "Palindrome"
    else:
        return "nope"
        
print(isPalindrome(input("Enter a word: ")))