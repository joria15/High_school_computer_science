"""
author: Anthony Antczak
date: 09/19/2025
project_unit_0 - Book Library
"""

#import libraries for code
import questionary, os
from datetime import datetime

#sort the library
def bubble_sort(library):
    ''' Sorts the library by lowest to highest
    >>>bubble_sort([b, a, c]):
    [a, b, c]
    >>>bubble_sort([2, 1, 3]):
    [1, 2, 3]
    '''
    #sorts from lowest to highest
    #processing
    for i in range(len(library)):
        for j in range(len(library)-1):
            if library[j] > library[j + 1]:
                library[j], library[j+1] = library[j+1], library[j]
    #output
    return library

#show the menu with the actions of which the user can choose from
def menu():
    ''' Shows a menu of options to choose from, use arrows to move and enter to chose
    >>>menu():
    Library: What would you like to do today?:
  >>{Check current library}
    {Add a book}
    {Search a book by: (title/author/title & author)}
    {Buy a book}

    {Work}
    {Check balance & time worked}
    {Current bonus multiplier & pay}

    {Exit}
   
    '''
    #input
    #processing
    option = questionary.select(
        "Library: What would you like to do today?",
        choices= ["{Check current library}", "{Add a book}", "{Search a book by: (title/author/title & author)}", "{Buy a book} \n",
        "{Work}", "{Check balance & time worked}", "{Current bonus multiplier & pay} \n", "{Exit}"]
        ).ask()
    #output
    return option

#--Column 1--#
#------Add a book------#
def add_book(library):
    ''' You will be asked to give the name of a book, the author and its cost, and will document the time
        the book was added
    >>>add_book(Title: King Lear, Author: Shakespeare, Cost: 10):
    [Title: King Lear, Author: Shakespeare, Cost: 10$, Import time: 2025-09-29 PM:07:52]
    >>>add_book(Title: Crime and punishment, Author: Dostoevksy, Cost: 5):
    [Title: Crime and punishment, Author: Dostoevksy, Cost: 5$, Import time: 2025-09-29 PM:07:53]

    '''
    #ask wether the person will want to add the book or go back to the menu
    #input
    options = questionary.select(
    "Would you like to add a book to the library?",
    choices= ["{Add a book}", "{Go back}"]
    ).ask()
    
    #processing
    #decided to add a book
    if options == "{Add a book}":

        book = []

        #title name
        #input
        #processing
        add_title = str(input("Name of title: "))
        titler = f"Title: {add_title}"
        book.append(titler)

        #author name
        #input
        #processing
        add_author = str(input("Name of author: "))
        autholer = f"Author: {add_author}"
        book.append(autholer)
       
       #cost of book
       #input
       #processing
        cost = int(input("Price($): "))
        book.append(cost)


        #time the book was added to the |year/month/day/hour/minute|
        #processing
        now = datetime.now()
        time = f"Import time: {now.strftime('%Y-%m-%d %p:%I:%M')}"
        book.append(time)

        #add the book to the list
        #processing
        library.append(book)

        #os system, it will delete the prior text in the terminal
        #it calls the os system and 'nt' tells the computer it is a windows computer, then 'cls' and 'clear'
        #clears the text from before
        #processing
        os.system('cls' if os.name == 'nt' else 'clear')

    #processing
    #if go back is chosen, it will return the user to the menu
    elif options == "{Go back}":
        #os system clears all prior text
        os.system('cls' if os.name == 'nt' else 'clear')
        #calls back the menu
        #output
        return menu()

#------search for a book------#
def search(library):
    ''' This will search for the book in the library by title/author/author & title
    >>>search([Title: a, Author: a]):
    inputfor title or author = a -> [Title: a, Author: a]
    >>>search([Title: king Lear, Author: Shakespeare ]):
    input for title and author = kin, Shake -> [Title: king Lear, Author: Shakespeare ]
    '''
    #options on how you want to search for the book
    #input
    options = questionary.select(
        "How would you like to search for a book?",
        choices= ["{By title}", "{By author}", "{By title & author}", "{Go back}"]
    ).ask()

    #search for the book by title
    #takes your input and tries to match it for any books in library at index 0 which is where the titles are in the list
    if options == "{By title}":
        #input
        title = input("What title are you looking for?: ")
        #processing
        for book in library:
            if title in book[0]:
                #output
                print("")
                print(book)
            #if there are no matching books then tell the user there is no related search
            #processing
            elif title not in book[0]:
                #output
                print("")
                print("{" "There are no titles related to your search" "}" "\n")

    #search for the book by author
    #takes your input and tries to match for any authors in the library at index 1 which is where the authors are in the list
    elif options == "{By author}":
        #input
        author = input("What author are you looking for?: ")
        #processing
        for book in library:
            if author in book[1]:
                #output
                print("")
                print(book)

            #if there are no matching authors then tell the user that there are no related searches
            #processing
            elif author not in book[1]:
                #output
                print("")
                print("{" "There are no authors related to your search" "}" "\n")

    #searched by title and author for a more deeper search than just by title or author
    elif options == "{By title & author}":
        #input
        title_book = input("What title are you looking for?: ")
        author_book = input("What author are you looking for?: ")

        #similarly to both the title and author search, it is both incorporated into one
        #it is just the first two but put together
        #processing
        for book in library:
            #if the title or author is in the library
            if title_book in book[0] or author_book in book[1]:
                #output
                print("")
                print(book)

            #if neither are then there are no related searches
            #processing
            elif title_book not in book[0] and author_book in book[1]:
                #output
                print("")
                print("{" "There are no titles or authors related to your search" "}" "\n")

    #if it is chosen to go back then the user is returned to the menu
    #processing
    elif options == "{Go back}":
        #output
        return menu()

#------buy a book------#
def buy_book(library, wallet):
    ''' This function allows the user to buy a book from the library with their currency, then the book is added to their
        inventory and removed from the library
    >>>buy_book({yes} -> {Title: King Lear, Author: Shakespeare, cost: 10$}):
    Inventory.txt -> appends the book -> Library = [] (removes the book)
    (case scenario: wallet = 5$ -> {Title: King Lear, Author: Shakespeare, cost: 10$} -> Insufficient funds) -> returns to menu
    >>>buy_book({Go back}):
    returns to menu
'''
    #choose wether to go back to the menu or buy a book
    #input
    option = questionary.select(
        "Would you like to buy a book today?",
        choices= ["{Yes}", "{Go back}"]
    ).ask()

    #continue to buy a book if yes is chosen
    #processing
    if option == "{Yes}":
        #create a list for choices
        shop = []
        #turn the books in the library into a text format to be able to be displayed in the choices
        for book in library:  
            #turn into text format
            text = f"{book[0]} | {book[1]} | Cost: {book[2]}$"
            shop.append(text)

        #display the list of text formatted books
        #input
        buy = questionary.select(
            "Which book would you like to buy today?",
            choices=shop
        ).ask()

        #processing
        #will be used to take the placeholder of a book at a certain index to contain the users choice
        chosen = None  
        #use the text format again to match at which index from the book matches the one from the choice chosen by the user
        #then chosen will equal it so I can get data from that book
        for book in library:
            text = f"{book[0]} | {book[1]} | Cost: {book[2]}$"
            if text == buy:
                chosen = text

            #processing
            #if purchasable, buy it and append it to the users inventory and remove it from the library
            if wallet >= book[2]:
                wallet -= book[2]
                with open("Inventory.txt", "a") as f:
                    f.write(chosen + "\n")
                library.remove(book)

            #else, print that the user does not have enough and return to the menu
            else:
                #output
                print("{" "Insufficient funds" "}")
                print("")
                return menu()

    #if the user wants to go back then return them to the menu 
    #processing
    elif option == "{Go back}":
        #output
        return menu()
    

#--Column 2--
#------work to earn currency and achieve bonus money------#
def work(wallet, work_lst, tries):
    ''' Work to earn currency and gain bonuses by how many times you worked and
    to earn more and buy books, considering also the history of when you have worked
    >>>work(0.00$, [], 0):
    4.00$, [Your current balance is: 4.00$ & the last time you worked is at Time: 2025-09-29 PM:07:44], 1
    >>>work(4,00$, [], 1):
    8.00$, [Your current balance is: 8.00$ & the last time you worked is at Time: 2025-09-29 PM:07:45], 2
    '''
    #processing

    #count how many times you have worked
    tries += 1

    #for every three times you have worked you gain a 0.10% bonus to your earn
    #it gets tries and divides by three to see how many times you worked in multiples of three
    #then it uses that number to add to your bonus multiplier by how many times you have worked in multiples of three
    bonus_multiplier = 1.00
    bonus_count = tries//3
    for i in range(bonus_count):
        bonus_multiplier += 0.10

    #you make 4.00$ by base value
    gain = 4.00
    #multiply your earn by the bonus_multiplier amount calculated from before
    bonus_amount = gain * bonus_multiplier
    #add to your wallet the amount you have made
    earned = wallet + bonus_amount

    #time module used to add to the history of when you have worked in |year/month/day/hour/minute| format
    now = datetime.now()
    time = f"Time: {now.strftime('%Y-%m-%d %p:%I:%M')}"

    #create a format to show when you have worked and how much is in your current balance after working
    check_in = f"Your current balance is: {round(earned, 2)}$ & the last time you worked is at {time}"

    #add to a list the check_in format to be seen as history whenever the user wants to see it
    work_lst.append(check_in)

    #return the money earned, the current bonus multiplier, how much the person will make each time they work,
    #and the amount of tiems worked
    return earned, bonus_multiplier, bonus_amount, tries


def main():
    #--column 1--#
    #library with books
    library = []
    #--column 2--#
    #amount of times worked
    tries = 0
    #carries the current balance and work time history
    work_lst = []
    #current balance
    wallet = 0.00
    #base money earned amount when working
    make = 4.00
    #how much earned when working
    bonus = 0.00
   
   #stays in the menu loop of options until you exit
   #you do one activity, and returns to menu to do another until user exits
   #processing
    while True:

        #calls the menu function to display options
        #output
        opt = menu()
        #--column 1--
        #check the current books in the library
        #processing
        if opt == "{Check current library}":
            #if there are no books then tell the user that there are no books because the length of the list is zero
            if len(library) == 0:
                #output
                print("{" "There are currently no books in the library" "}" "\n")
            else:
                #sorts the library by alphabetical and numerical order from lowest to highest
                #processing
                bubble_sort(library)
                #prints the books in the library by one line at a time
                for line in library:
                    #output
                    print("{",f"{line[0]} |", f"{line[1]} |", f"Cost: {line[2]}$ |", f"{line[3]}","}")

        #goes to the add_book() function
        #processing
        elif opt == "{Add a book}":
            add_book(library)

        #goes to the search() function
        #processing
        elif opt == "{Search a book by: (title/author/title & author)}":
            search(library)

        #goes to the buy_book() function
        #processing
        elif opt == "{Buy a book} \n":
            buy_book(library, wallet)  

        #--column 2--
        #goes to the work() function
        #processing
        elif opt == "{Work}":
            #from the returns, it gives the wallet the current balance, the current bonus_multiplier
            #how much you make each time you work, including the bonus_multiplier add on
            #and how many times you have worked
            wallet, bonus, make, tries = work(wallet, work_lst, tries)

        #will print the list that shows the history of when you have worked and your current balance at that time
        #processing
        elif opt == "{Check balance & time worked}":
            #if there is no work history because you have worked 0 times, then tell the user there is no current data
            if len(work_lst) == 0:
                #output
                print("{" "There is no current data" "}")
                print("")
            #print the work history result by one line at a time
            else:
                #processing
                for worked in work_lst:
                    #output
                    print("{" + worked + "}")
                print("")

        #shows the current bonus_multiplier and pay for everytime you work
        #processing
        elif opt == "{Current bonus multiplier & pay} \n":
            #if there is no current bonus
            if bonus == 0:
                #output
                print("{" f"Your current bonus multiplier is: 1.00x & make {round(make, 2)}$ each time you work" "}" "\n")
            #else show the current bonus_multiplier and how much the user makes everytime they work
            #output
            else:
                print("{" f"Your current bonus multiplier is: {bonus}x & make {round(make, 2)}$ each time you work" "}" "\n")
        
        #if the user chooses to exit
        #processing
        elif opt == "{Exit}":
            #clear the current txt file to renew it for the next time they play by passing it
            with open("Inventory.txt", "w") as f:
                pass
            #output
            print("Thank you for brousing with us.")
            #stop the loop
            break

if __name__ == '__main__':
    
    main()
