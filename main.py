import re

def openFile():
    with open("bestseller.txt") as file:
        return file.readlines()


def yearRange():
    book_list = []
    starting_year = int(input("Enter beginning year: "))
    ending_year = int(input("Enter ending year: "))
    books = openFile()
    for book in books:
            year = int(book.split("\t")[3].split("/")[-1])
            if year >= starting_year and year <= ending_year:
                book_list.append(book)
    if not book_list:
        print(f"No books found between {starting_year} and {ending_year}")
    else:
        print(f"All Titles between {starting_year} and {ending_year}")
        for book in book_list:
            print(book)
    
def monthYear():
    book_list = []
    month = int(input("Enter month (as a number 1-12): "))
    year = int(input("Enter year: "))
    books = openFile()
    for book in books:
        b_month = int(book.split("\t")[3].split("/")[0])
        b_year = int(book.split("\t")[3].split("/")[-1])
        if month == b_month and year == b_year:
            book_list.append(book)
    if not book_list:
        print(f"No books found in month{month} of {year}")
    else:
        print(f"All Titles in the month {month} of {year}: ")
        for book in book_list:
            print(book)

def searchAuthor():
    #  Enter an author's name (or part of a name): 
    author = input("Enter an author's name (or part of a name): ")
    books = openFile()
    author_list = []
    for book in books:
        bk_author = book.split("\t")[1]
        regex  = re.compile(author, re.IGNORECASE)
        if regex.search(bk_author):
            author_list.append(book)
    if author_list:
        print("\n".join(author_list)) 
    else:
        print(f"No book with {author} found.")          
  

        
def searchTitle():
    # Enter a title (or part of a title):
    title_list = []
    title = input("Enter a title (or part of a title): ")
    books = openFile()
    for book in books:
        bk_title = book.split("\t")[0]
        reg = re.compile(title, re.IGNORECASE)
        if reg.search(bk_title):
            title_list.append(book)
    if title_list:
        print("\n".join(title_list))
    else:
        print(f"{title} was not found.")


while True:
    user_input = input("""
What would you like to do?
1: Look up year range
2: Look up month/year
3: Search for author
4: Search for title
Q: Quit
    """).strip()

    if user_input == "1":
        yearRange()
    if user_input == "2":
        monthYear()
    if user_input == "3":
        searchAuthor()
    if user_input == "4":
        searchTitle()
    if user_input == "q":
        print("Exiting menu ...")
        break

                 
