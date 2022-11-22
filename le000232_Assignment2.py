#Written in Python

class bookInfo:
    def __init__(self, Title, Author, UserRating, Reviews, Price, PublicationYear, Genre):
        self.Title = Title
        self.Author = Author
        self.UserRating = UserRating
        self.Reviews = Reviews
        self.Price = Price
        self.PublicationYear = PublicationYear
        self.Genre = Genre

    def __repr__(self):
        return '{:<85}|{:<40}|{:<15}|{:<10}|{:<10}|{:<25}|{:<15}'.format(self.Title, self.Author, self.UserRating, self.Reviews, self.Price,
                                             self.PublicationYear, self.Genre)
        # Properly stores elements.
        # Formats and spaces element when printed.


def headerFormat():
    print("\n")
    print('{:<85}|{:<40}|{:<15}|{:<10}|{:<10}|{:<25}|{:<15}'.format("Title", "Author", "User Rating", "Reviews", "Price", "Year of Publication", "Genre"))
    print("-"*205)


def SearchByYear(sortedByDate):
    yearBegin = int(input("Enter the start year: "))
    yearEnd = int(input("Enter the end year: "))

    nSearchResults = 0
    for el in sortedByDate:
        if (el.PublicationYear >= yearBegin) and (el.PublicationYear <= yearEnd):
            nSearchResults +=1
            if nSearchResults == 1:        # To prevent the header from being printed every time a search result is found.
                headerFormat()             # The header is printed first assuming there's a sucessful search.
            print(el)                      # After, only searches results will be printed. Format reasons.
    print("\n")
    if nSearchResults == 0:
        print("Oops couldn't find search result.\n")


def SearchByRating(bookList):
    searchRating = input("Enter the rating: ")
    searchRating = float(searchRating)

    nSearchResults = 0
    for el in bookList:
        if el.UserRating == searchRating:
            nSearchResults += 1
            if nSearchResults == 1:        # To prevent the header from being printed every time a search result is found.
                headerFormat()             # The header is printed first assuming there's a sucessful search.
            print(el)                      # After, only searches results will be printed. Format reasons.
    print("\n")
    if nSearchResults == 0:
        print("Oops couldn't find search result.\n")  # if no search is found, it will print said message.


def SearchByAuthor(booklList):
    authorName = str(input("Enter the author name: "))
    authorNameCap = authorName.capitalize()

    nSearchResults = 0
    for el in booklList:
        if (el.Author.__contains__(authorName) == True) or (el.Author.__contains__(authorNameCap) == True):
            nSearchResults += 1
            if nSearchResults == 1:        # To prevent the header from being printed every time a search result is found.
                headerFormat()             # The header is printed first assuming there's a sucessful search.
            print(el)                      # After, only searches results will be printed. Format reasons.
    print("\n")
    if nSearchResults == 0:
        print("Oops couldn't find search result.\n")  # if no search is found, it will print said message.


def SearchByTitle(bookList):
    TitleName = str(input("Enter the author name: "))
    TitleNameCap = TitleName.capitalize()

    nSearchResults = 0
    for el in bookList:
        if (el.Title.__contains__(TitleName) == True) or (el.Title.__contains__(TitleNameCap) == True):
            nSearchResults += 1
            if nSearchResults == 1:        # To prevent the header from being printed every time a search result is found.
                headerFormat()             # The header is printed first assuming there's a sucessful search.
            print(el)                      # After, only searches results will be printed. Format reasons.
    print("\n")
    if nSearchResults == 0:
        print("Oops couldn't find search result.\n")  # if no search is found, it will print said message.



# -----------------------------------------------

listOfBooks = []

myfile = open('booklist.txt', 'r', encoding="utf8")   # open file
myfile.seek(0)                                        # start at the beginning of the file

for line in myfile:
    title, author, userRating, reviews, price, publicationYear, genre = line.split(",")                                      # obtains each element seperated by a comma in booklist.txt.
    if len(title) > 75:                    # if the length of a title is more than 75 characters, stop it at that.
        title = title[:75] + "..."         # then append "..." to the end of the cut-off title.
    listOfBooks.append(bookInfo(title, author, float(userRating), reviews, price, int(publicationYear), genre.strip("\n")))  # creates class objects with said elements. Appends this class object to listOfBooks so it can be stored.

sorted_by_date = sorted(listOfBooks,key=lambda bookInfo:bookInfo.PublicationYear)                                            # Sort list by date to make it look neat and more readable to the user.

#-----------------------------------------------------------------------------



print("\nLibrary search\n")
userInput = None

while (userInput == None) or (userInput != 'Q'):
    print("1 Enter year range")
    print("2 Enter minimum rating")
    print("3 Search for author")
    print("4 Search for title")
    print("Q Quit\n")

    userInput = input("Select option #: ") # Takes userInput with no data type specified.
    try:                                   # Try & except statement obtains the correct data type for userInput.
        userChoice = int(userInput)        # Transforms input into an int. If it can't be converted to int, ...
    except:                                # ... it will be converted to str in the expect statement.
        userChoice = str(userInput)

    if userChoice == 1:
        SearchByYear(sorted_by_date)
    elif userChoice == 2:
        SearchByRating(sorted_by_date)
    elif userChoice ==3:
        SearchByAuthor(sorted_by_date)
    elif userChoice == 4:
        SearchByTitle(sorted_by_date)
    elif (userChoice== 'Q') or (userChoice == 'q'):
        exit()
    else:
        print("\n\nInvalid response. Please try again\n")

myfile.close()
