# Write Your Code Here
# NotebookApp.iopub_data_rate_limit=10000000.0
# -----------------------------------------------

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


def headerFormat():
    print("\n")
    print('{:<85}|{:<40}|{:<15}|{:<10}|{:<10}|{:<25}|{:<15}'.format("Title", "Author", "User Rating", "Reviews", "Price", "Year of Publication", "Genre"))
    print("-"*205)

# def checkIfSearchResultIsEmpty(nSearches):
#     if nSearches == 0:
#         print("Oops couldn't find search result.")


def SearchByYear(sortedByDate):
    yearBegin = int(input("Enter the start year: "))
    yearEnd = int(input("Enter the end year: "))

    nSearchResults = 0
    for el in sortedByDate:
        if (el.PublicationYear >= yearBegin) and (el.PublicationYear <= yearEnd):
            nSearchResults +=1
            if nSearchResults == 1:
                headerFormat()
            print(el)
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
            if nSearchResults == 1:        # if a single search result is found, header format will be executed one time
                headerFormat()             #
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
            if nSearchResults == 1:        # if a single search result is found, header format will be executed one time
                headerFormat()             #
            print(el)                      # After, only searches results will be printed. Format reasons.
    print("\n")
    if nSearchResults == 0:
        print("Oops couldn't find search result.\n")  # if no search is found, it will print said message.


def SearchByTitle(bookList):
    TitleName = str(input("Enter the author name: "))
    TitleNameCap = TitleName.capitalize()

    headerFormat()
    nSearchResults = 0
    for el in bookList:
        if (el.Title.__contains__(TitleName) == True) or (el.Title.__contains__(TitleNameCap) == True):
            nSearchResults += 1
            if nSearchResults == 1:        # if a single search result is found, header format will be executed one time
                headerFormat()             #
            print(el)                      # After, only searches results will be printed. Format reasons.
    print("\n")
    if nSearchResults == 0:
        print("Oops couldn't find search result.\n")  # if no search is found, it will print said message.



# -----------------------------------------------

listOfBooks = []

myfile = open('booklist.txt', 'r', encoding="utf8")
myfile.seek(0)

for line in myfile:

    lineStr = line

    title, author, userRating, reviews, price, publicationYear, genre = lineStr.split(",")
    if len(title) > 75:                    # if the length of a title is more than 75 characters, stop it at that.
        title = title[:75] + "..."         # then add "..."
    listOfBooks.append(bookInfo(title, author, float(userRating), reviews, price, int(publicationYear), genre.strip("\n")))

sorted_by_date = sorted(listOfBooks,key=lambda bookInfo:bookInfo.PublicationYear)  # Purpose: to make it look neat

#-----------------------------------------------------------------------------



print("\nLibrary search\n")
userInput = None

while (userInput == None) or (userInput != 'Q'):
    print("1 Enter year range")
    print("2 Enter minimum rating")
    print("3 Search for author")
    print("4 Search for title")
    print("Q Quit\n")

    userInput = input("Select option #: ")
    try:
        userChoice = int(userInput)        # if it can't be converted to int,
    except:                                #                        it will be converted to str in the expect statement.
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
