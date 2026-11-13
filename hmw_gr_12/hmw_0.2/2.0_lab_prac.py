"""
Add your header comments here.
"""


# ============================
# PART 1: CORE FUNCTIONALITY
# ============================


def initialize_library() -> dict[str, dict[str, str | int]]:
    """
    Creates and returns a library catalog dictionary with user input.
    Prompts for ISBN, title, author, year, copies for at least 3 books.
    """
    library_catalog: dict[str, dict[str, str | int]] = {}
   
    # TODO: Implement loop to get at least 3 books from user
    # Hint: You can use a for loop with range(3) or while loop with yes/no prompt
    for i in range(3):
        isbn = str(input("Atleast an 8-digit ISBN code: "))
        title = str(input("Title of book: "))
        author = str(input("Author of book: "))
        year = int(input("Year the book was written: "))
        copies = int(input("Amount of copies: "))
        library_catalog[isbn] = {"title": title, "author": author, "year": year, "copies": copies}
    return library_catalog


def search_book(library_catalog: dict[str, dict[str, str | int]], isbn: str) -> dict[str, str | int] | None:
    """
    Searches for and displays a book by ISBN.
    Prints book info or "Book not found".
    """
    # TODO: Use .get() method to retrieve book
    # TODO: If found, print all book information in readable format
    # TODO: If not found, print "Book not found"
   
    book = library_catalog.get(isbn, "Book not found")
    print(book)




def add_book(library_catalog: dict[str, dict[str, str | int]], isbn: str,
             title: str, author: str, year: int, copies: int) -> bool:
    """
    Adds a new book to the library catalog with basic validation.
    Checks if ISBN exists, validates year range and copies.
    Prints status message and returns True if successful, False otherwise.
    """
    # TODO: Check if ISBN already exists using 'in' operator
    # TODO: Check if year is between 1800 and 2025
    # TODO: Check if copies is >= 0
    # TODO: If checks pass, add book and return True
    # TODO: Otherwise print error and return False

    if isbn in library_catalog.keys():
        print("Book already exists")
        return False
    if 1800 > year or year > 2025:
        print("Non existant or outdated")
        return False
    if copies < 1:
        print("No copies exist")
        return False
    
    library_catalog[isbn] = {"title": title, "author": author, "year": year, "copies": copies}
    return True





# ============================
# PART 2: VALIDATION AND SEARCH FEATURES
# ============================


def validate_isbn(isbn: str) -> bool:
    """
    Validates ISBN format (must start with "ISBN" followed by digits, min length 8).
    """
    # TODO: Check if ISBN starts with "ISBN" using .startswith()
    # TODO: Check if length is at least 8
    # TODO: Check if characters after "ISBN" are all digits using slicing and .isdigit()

    if not(isbn.startswith("ISBN")):
        print("ISBN must be starting letters")
        return False
    if len(isbn[5:]) < 8:
        print("You must have atleast 8-digits")
        return False
    if not(isbn[5:].isdigit()):
        print("All the digits must be numbers")
        return False
    return True




def validate_title(title: str) -> bool:
    """
    Validates book title (not empty, contains at least one letter).
    """
    # TODO: Strip whitespace and check if not empty
    # TODO: Check if title contains at least one letter character
    # Hint: Loop through characters and use .isalpha()
    count = 0
    titles = title.replace(" ", "")
    for i in range(len(titles)):
        if titles[i].isalpha():
            count += 1

    if len(titles) < 1 or count < 1:
        return False
   
    return True


def search_by_author(library_catalog: dict[str, dict[str, str | int]], author_name: str) -> list[tuple[str, str]]:
    """
    Searches for all books by a specific author (case-insensitive).
    Returns sorted list of tuples (isbn, title).
    """
    # TODO: Create empty list for results
    # TODO: Loop through library_catalog.items()
    # TODO: Compare author names using .lower() for case-insensitive match
    # TODO: If match, add (isbn, title) tuple to list
    # TODO: Sort the list alphabetically by title (second element)
    # TODO: Return the sorted list
   
    results = []


    for isbn, book in library_catalog.items():
        if author_name.lower() in book["author"].lower():
            res = (isbn, book["title"])
            results.append(res)
            
        for i in range(len(results)):
            for j in range(len(results)-1):
                if results[j][1] > results[j+1]:
                    results[j], results[j+1] = results[j+1], results[j]
                results[j] = tuple(results[j])
        results[len(results)-1] = tuple(results[len(results)-1])
    return results
                
def checkout_book(library_catalog: dict[str, dict[str, str | int]], isbn: str) -> bool:
    """
    Checks out a book (decreases copies by 1).
    Returns True if successful, False otherwise. Prints status message.
    """
    # TODO: Check if ISBN exists in library_catalog
    # TODO: Check if copies > 0
    # TODO: If checks pass, decrease copies by 1 and print success message
    # TODO: Return True if successful, False otherwise
   

    if isbn not in library_catalog:
        print("IBSN code Does not exit")
        return False

    if library_catalog[isbn]["copies"] <= 0:
        print("There are no existing copies of the book")
        return False
    
    library_catalog[isbn]["copies"] -= 1

    print("Book checked out succesfully")
    print(f"There are now {library_catalog[isbn]["copies"]} remaining copies")
    return True


# ============================
# PART 3: INTERACTIVE SYSTEM AND ADVANCED FEATURES
# ============================


def display_menu() -> None:
    """
    Displays the library menu options.
    """
    print("\n=== Library Management System ===")
    print("1. Search for a book")
    print("2. Add new book")
    print("3. Check out a book")
    print("4. Return a book")
    print("5. Search by author")
    print("6. View library statistics")
    print("7. Find popular books")
    print("8. Exit")




def return_book(library_catalog: dict[str, dict[str, str | int]], isbn: str) -> bool:
    """
    Returns a book (increases copies by 1).
    Returns True if successful, False otherwise. Prints status message.
    """
    # TODO: Check if ISBN exists in library_catalog
    # TODO: If exists, increase copies by 1 and print success message
    # TODO: Return True if successful, False otherwise
   
    if isbn in library_catalog.keys():
        print("Thank you for returning")
        library_catalog[isbn]["copies"] += 1
        return True
    
    print("ISBN code does not exist")
    return False




def generate_statistics(library_catalog: dict[str, dict[str, str | int]]) -> tuple[int, int, float, str]:
    """
    Generates statistics about the library catalog.
    Returns tuple (total_books, total_copies, avg_year, common_author).
    """
    # TODO: Calculate total number of unique books
    # TODO: Calculate total copies across all books
    # TODO: Calculate average publication year (round to 1 decimal)
    # TODO: Find most common author (author with most books)
    # Hint: Create a dictionary to count books per author
    # TODO: Return tuple with all statistics

    maxxed = 0

    total_books = len(library_catalog)
    total_copies = sum(book["copies"] for book in library_catalog.values())
    avg_year = round(sum(book["year"] for book in library_catalog.values())/total_books, 1)

    author_count = {}
    for book in library_catalog.values():
        author = book["author"]
        if author in author_count:
            author_count[author] += 1
        else:
            author_count[author] = 1
    for writer, copie in author_count.items():
        if copie > maxxed:
            common_author = writer
            maxxed = copie
        
    return (total_books, total_copies, avg_year, common_author)





def group_by_decade(library_catalog: dict[str, dict[str, str | int]]) -> dict[str, list[dict[str, str | int]]]:
    """
    Groups books by decade WITHOUT creating aliases.
    Returns dict {"1920s": [book_dicts], "1960s": [book_dicts], ...}
    """
    # TODO: Create empty dictionary for results
    # TODO: Loop through library_catalog.items()
    # TODO: Calculate decade: (year // 10) * 10, then format as "1920s"
    # TODO: For each book, create a COPY using .copy() method
    # TODO: Add the copy to the appropriate decade list
    # TODO: Return the grouped dictionary
   
    results = {}
    for isbn, data in library_catalog.items():
        decade = (data["year"] // 10) * 10
        if f"{decade}s" not in results:
            results[f"{decade}s"] = [data.copy()]
        else:
            results[f"{decade}s"].append(data.copy())
    return results




def find_popular_books(library_catalog: dict[str, dict[str, str | int]], min_copies: int) -> list[tuple[str, str, int]]:
    """
    Finds books with at least min_copies available.
    Returns list of tuples (isbn, title, copies) sorted by copies descending.
    """
    # TODO: Create empty list for results
    # TODO: Loop through library_catalog.items()
    # TODO: If copies >= min_copies, add (isbn, title, copies) to list
    # TODO: Sort by copies in descending order
    # Hint: Use sorted() with key=lambda x: x[2], reverse=True
    # TODO: Return the sorted list
   
    results = []
    for isbn, data in library_catalog.items():
        copies = data["copies"]
        if copies >= min_copies:
            results.append([isbn, data["title"], copies])
    for i in range(len(results)):
        for j in range(len(results)-1):
            if results[j][2] > results[j+1][2]:
                results[j], results[j+1] = results[j+1], results[j]
    results.reverse()
    return results




def main() -> None:
    """
    Main function that runs the interactive library menu system.
    """
    print("Welcome to the Library Management System!")
    print("Let's initialize your library catalog.\n")
   
    # Initialize the library catalog with user input
    library_catalog: dict[str, dict[str, str | int]] = initialize_library()
   
    # TODO: Create a while loop that continues until user chooses to exit
    # TODO: Display menu using display_menu()
    # TODO: Get user choice
    # TODO: Use if/elif to handle each menu option:
    #       1. Search for a book
    #       2. Add new book
    #       3. Check out a book
    #       4. Return a book
    #       5. Search by author
    #       6. View statistics (use tuple unpacking!)
    #       7. Find popular books (prompt for minimum copies)
    #       8. Exit
    # TODO: Handle invalid menu choices
    while True:
        display_menu()

        choice = (input("Enter your choice (1-8): "))

        if choice == "1":
            search_book(library_catalog, input("Enter ISBN: "))

        elif choice == "2":
            while True:
                isbn = str(input("Atleast an 8-digit ISBN code: "))
                if validate_isbn(isbn) == False:
                    continue
                break
            
            while True:
                title = str(input("Title of book (not empty): "))
                if validate_title(title) == False:
                    continue
                break
            
            author = str(input("Author of book: "))
            year = int(input("Year the book was written: "))
            copies = int(input("Amount of copies: "))

            add_book(library_catalog, isbn, title, author, year, copies)

        elif choice == "3":
            checkout_book(library_catalog, input("Enter ISBN: "))

        elif choice == "4":
            return_book(library_catalog, input("Enter ISBN: "))

        elif choice == "5":
            search_by_author(library_catalog, input("Enter author: "))

        elif choice == "6":
            total_books, total_copies, avg_year, common_author = generate_statistics(library_catalog)
            print(f"Total books: {total_books}; Total Copies: {total_copies}; Average year: {avg_year}")
            print(f"Common author: {common_author}")

        elif choice == "7":
            print(find_popular_books(library_catalog, input("Number of minimum copies: ")))

        elif choice == "8":
            break
        else:
            print("Invalid input, choice must be between (1-8)")

    print("\nThank you for using the Library Management System!")




# ============================
# TESTING CODE - DO NOT EDIT!
# ============================


def test_part1() -> None:
    """Test Part 1 functions."""
    print("=== PART 1 TESTS ===\n")
   
    # Test initialize_library
    library: dict[str, dict[str, str | int]] = initialize_library()
    print(f"\nInitialized {len(library)} books\n")
   
    # Test search
    if len(library) > 0:
        first_isbn: str = list(library.keys())[0]
        print(f"Searching for {first_isbn}:")
        search_book(library, first_isbn)
   
    # Test add
    print("\nTesting add_book:")
    result: bool = add_book(library, "ISBN999", "Test Book",
                           "Test Author", 2020, 5)
    print(f"Add successful: {result}")




def test_part2() -> None:
    """Test Part 2 functions."""
    print("\n=== PART 2 TESTS ===\n")
   
    # Test validation functions
    print("Testing validate_isbn:")
    print(f"  'ISBN12345': {validate_isbn('ISBN12345')} (should be True)")
    print(f"  '12345': {validate_isbn('12345')} (should be False)")
    print(f"  'ISBN1': {validate_isbn('ISBN1')} (should be False - too short)")
   
    print("\nTesting validate_title:")
    print(f"  'The Great Gatsby': {validate_title('The Great Gatsby')} (should be True)")
    print(f"  '': {validate_title('')} (should be False)")
    print(f"  '   ': {validate_title('   ')} (should be False)")
   
    # Create sample library for testing
    library: dict[str, dict[str, str | int]] = {
        "ISBN001": {"title": "The Great Gatsby", "author": "F. Scott Fitzgerald",
                    "year": 1925, "copies": 3},
        "ISBN002": {"title": "To Kill a Mockingbird", "author": "Harper Lee",
                    "year": 1960, "copies": 5},
        "ISBN003": {"title": "1984", "author": "George Orwell",
                    "year": 1949, "copies": 0}
    }
   
    # Test search by author
    print("\nTesting search_by_author:")
    books: list[tuple[str, str]] = search_by_author(library, "harper lee")
    print(f"  Books by Harper Lee: {books}")
   
    # Test checkout
    print("\nTesting checkout_book:")
    result1: bool = checkout_book(library, "ISBN001")
    print(f"  Checkout ISBN001: {result1} (should be True)")
    result2: bool = checkout_book(library, "ISBN003")
    print(f"  Checkout ISBN003: {result2} (should be False - no copies)")




def test_part3() -> None:
    """Test Part 3 functions."""
    print("\n=== PART 3 TESTS ===\n")
   
    # Create sample library
    library: dict[str, dict[str, str | int]] = {
        "ISBN001": {"title": "The Great Gatsby", "author": "F. Scott Fitzgerald",
                    "year": 1925, "copies": 3},
        "ISBN002": {"title": "To Kill a Mockingbird", "author": "Harper Lee",
                    "year": 1960, "copies": 5},
        "ISBN003": {"title": "1984", "author": "George Orwell",
                    "year": 1949, "copies": 2},
        "ISBN004": {"title": "Harry Potter", "author": "J.K. Rowling",
                    "year": 1997, "copies": 10},
        "ISBN005": {"title": "The Hobbit", "author": "J.R.R. Tolkien",
                    "year": 1937, "copies": 4}
    }
   
    # Test statistics
    print("Testing generate_statistics:")
    stats: tuple[int, int, float, str] = generate_statistics(library)
    if stats:
        total, copies, avg_year, author = stats
        print(f"  Total books: {total}, Total copies: {copies}")
        print(f"  Average year: {avg_year}, Most common author: {author}")
   
    # Test group by decade with aliasing check
    print("\nTesting group_by_decade (aliasing test):")
    grouped: dict[str, list[dict[str, str | int]]] = group_by_decade(library)
    if grouped:
        print(f"  Decades found: {list(grouped.keys())}")
        original_title: str = str(library["ISBN001"]["title"])
        # Try to modify a grouped copy
        if "1920s" in grouped and len(grouped["1920s"]) > 0:
            grouped["1920s"][0]["title"] = "CHANGED TITLE"
            print(f"  Original title: {library['ISBN001']['title']}")
            print(f"  Modified copy: {grouped['1920s'][0]['title']}")
            if original_title == library["ISBN001"]["title"]:
                print("  ✓ No aliasing! Original unchanged.")
            else:
                print("  ✗ Aliasing detected! Original was modified.")
   
    # Test find popular books
    print("\nTesting find_popular_books:")
    popular: list[tuple[str, str, int]] = find_popular_books(library, 4)
    if popular:
        print(f"  Books with 4+ copies:")
        for isbn, title, copies in popular:
            print(f"    {title}: {copies} copies")




if __name__ == "__main__":
    # Uncomment the tests you want to run:
   
    # For Part 1 testing:
    #test_part1()
   
    # For Part 2 testing:
    #test_part2()
   
    # For Part 3 testing:
    #test_part3()
   
    # For Part 3 interactive menu:
    #main()
   
    print("Uncomment the test functions or main() to run the program!")



